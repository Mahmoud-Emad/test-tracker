"""Everything related to TestRuns"""
from os import truncate
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from server.test_tracker.models.project import TestCases, TestRun, TestSuites





class LastWeekTestRunReportSheetSerializer(ModelSerializer):
    """
    This class is used to serialize the last week test run report sheet
    """
    not_run = SerializerMethodField()
    passed = SerializerMethodField()
    failed = SerializerMethodField()
    skipped = SerializerMethodField()

    class Meta:
        model = TestRun
        fields = (
            'id',
            'title',
            'test_cases_count',
            'test_suites_count',
            'test_runs_count'
        )

    def get_not_run(self, obj):
        return obj.test_cases.count()

    def get_passed(self, obj):
        return obj.test_suites.count()

    def get_failed(self, obj):
        return obj.test_runs.count()
    
    def get_skipped(self, obj):
        return obj.test_runs.count()

class TestRunsSerializer(ModelSerializer):
    """Test run serializer class"""
    assigned_user = SerializerMethodField()
    total_test_cases = SerializerMethodField()
    passed = SerializerMethodField()
    failed = SerializerMethodField()
    skipped = SerializerMethodField()
    not_run = SerializerMethodField()
    completed = SerializerMethodField()
    created = SerializerMethodField()
    modified = SerializerMethodField()

    class Meta:
        model = TestRun
        fields = [
            'id','title','test_suites','total_test_cases','assigned_user',
            'passed', 'failed','skipped', 'not_run', 'completed','status',
            'created','modified'
        ]

    def get_created(self, obj):
        """Method to get the created date"""
        return obj.created.date()
    
    def get_modified(self, obj):
        """Method to get the modified date"""
        return obj.modified.date()

    def test_cases(self, test_suites: TestSuites) -> TestCases:
        """Service method to return all of test cases based on test suite"""
        return TestCases.objects.filter(test_suite__in=test_suites.all())

    def get_total_test_cases(self, obj: TestRun) -> int:
        """
        This method is used to get the total number of test cases
        """
        return len(self.test_cases(obj.test_suites))

    def get_passed(self, obj: TestRun) -> int:
        """Return length of passed test cases"""
        return len(self.test_cases(obj.test_suites).filter(
                passed=True
            )
        )

    def get_failed(self, obj: TestRun) -> int:
        """Return length of passed test cases"""
        return len(self.test_cases(obj.test_suites).filter(
                failed=True
            )
        )

    def get_skipped(self, obj: TestRun) -> int:
        """Return length of passed test cases"""
        return len(self.test_cases(obj.test_suites).filter(
                skipped=True
            )
        )

    def get_not_run(self, obj: TestRun) -> int:
        """Return length of passed test cases"""
        return len(self.test_cases(obj.test_suites).filter(
                run=False
            )
        )

    def get_completed(self, obj: TestRun) -> int:
        """Return length of passed test cases"""
        if  self.get_not_run(obj) == 0:
            return f"100.0%"
        return f"{round(len(self.test_cases(obj.test_suites).filter(completed=True)) / len(self.test_cases(obj.test_suites)) * 100, 1)}%"

    def get_assigned_user(self, obj):
        """Return assigned user"""
        from server.test_tracker.serializers.member import ProjectTeamSerializer
        return ProjectTeamSerializer(obj.assigned_user).data
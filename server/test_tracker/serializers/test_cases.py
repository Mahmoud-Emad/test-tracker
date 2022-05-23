"""Everything related to TestCases"""


from server.test_tracker.models.project import TestCases
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from server.test_tracker.serializers.requirement import RequirementsSerializer





class TestCaseSerializer(ModelSerializer):
    """class TestCaseSerializer to serialize the test case obj"""
    requirement = SerializerMethodField()
    created = SerializerMethodField()

    class Meta:
        model = TestCases
        exclude = (
            'verify_requirement', 'test_suite',
            'comments', 'passed', 'failed', 'skipped', 'run', 'completed'
        )

    def get_requirement(self, obj):
        """Method to get the requirement obj"""
        return RequirementsSerializer(obj.verify_requirement).data
    
    def get_created(self, obj):
        return obj.created.date()


class GetSingleTestCaseSerializer(ModelSerializer):
    """class TestCaseSerializer to serialize the test case obj"""
    requirement = SerializerMethodField()

    class Meta:
        model = TestCases
        fields = (
            'title', 'description', 'test_steps', 'expected_result',
            'requirement', 'test_suite','comments', 'passed', 'failed',
            'skipped', 'run', 'completed'
        )

    def get_requirement(self, obj):
        """Method to get the requirement obj"""
        return RequirementsSerializer(obj.verify_requirement).data
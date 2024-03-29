<script>
    import { onMount } from "svelte";
    import { Link } from "svelte-navigator";
    import { createEventDispatcher } from 'svelte';
    import axios from "../healpers/axios";
    import { inviteNewMemberFields, newMemberPermission } from "../healpers/fields";
    import { validateFields, claerFields } from "../healpers/validateFields"
    import { inviteNewMember } from "../healpers/api"
    import Alert from "../components/ui/Alert.svelte";
    import Modal from "../components/ui/Modal.svelte";

    import NavBar from "../components/NavBar.svelte";
    import Search from "../components/Search.svelte";
    import Input from "../components//ui/Input.svelte";
    import LoodingSpiner from "../components/ui/LoodingSpiner.svelte";
    import DeleteModal from "../components/ui/DeleteModal.svelte";
    import MemberCard from "../components/MemberCard.svelte";

    export let user;

    let members, membersCopy, thisMember, showModal, showAlert, _class, message;
    let showDeleteModal = false;

    const config = {
        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` },
    };

    let newMember = inviteNewMemberFields();
    let memberPermission = newMemberPermission();
    const dispatch = createEventDispatcher();

    function logger(_class_, _message_) {
        showAlert = true;
        _class = _class_;
        message = _message_;
    };

    onMount(async () => {
        try {
            const response = await axios.get("/members/all/", config);
            members = await response.data.results
            membersCopy = members;
        } catch (err) {
            if (err.response.status === 403) {
                window.location.href = "/not-found";
            }
        }
    });

    async function validateAndSubmit(){
        const response = await inviteNewMember(newMember);
        _class = response.class;
        message = response.message;
        logger(_class, message);
        if (response.data) {
            setTimeout(() => {
                showAlert = false;
                showModal = false;
                members.push(response.data);
                for (const filed in newMember) {
                    newMember[filed] = "";
                }
            }, 500);
        }
    }

    async function handleDelete(event) {
        const member = event.detail.obj;
        const indx = members.findIndex((v) => v.id === member.id);
        members = members;
        members.splice(indx, 1);
    }

    async function handleSearch(event) {
        const searchProjects = event.detail.objects;
        members = searchProjects;
    }

    function setMember(member) {
        thisMember = member;
        showDeleteModal = true;
    }

    function openAddMemberModal(member) {
        showModal = true;
    }
</script>

<svelte:head>
    <title>Test-Tracker | Members</title>
</svelte:head>

<section>
    {#if user}
        <NavBar {user} />
        <div class="container pt-4 pb-4">
            <div class="row">
                <div class="col-10">
                    <p class="h4 mb-2">
                        <strong class="h4 text-primary">All Members</strong>
                    </p>
                    {#if members && members.length > 0}
                        <p class="text-muted">
                            -- There are <strong class="text-primary">{members.length}</strong>
                            {user.total_projects === 1 ? "member" : "members"} registered
                        </p>
                    {/if}
                </div>
                <div class="col-2">
                    <button class="btn btn-primary" on:click={
                        () => {showModal = true}
                    }>
                        Invite member
                    </button>
                </div>
            </div>
            {#if members && members.length > 0}
                <div class="pt-4">
                    <p>Search Members</p>
                    <Search
                        request="/members/search/"
                        objects={members}
                        objectsCopy={membersCopy}
                        on:message={handleSearch}
                    />
                </div>
                <div class="pt-5">
                    <div class="row">
                        {#each members as member}
                            <MemberCard {member}>
                                <Link 
                                    to=""
                                    class="dropdown-item plus-hover drop-size" 
                                    on:click={setMember(member)}
                                    >Delete {member.first_name}
                                </Link>
                            </MemberCard>
                        {/each}
                    </div>
                </div>
            {:else}
                <Alert 
                    showAlert = {true} 
                    message = {"There are no members, try to invite someone"} 
                    _class = {"info"}
                />
            {/if}
        </div>
    {:else}
        <LoodingSpiner />
    {/if}
    <DeleteModal
        bind:showDeleteModal
        on:message={handleDelete}
        obj={thisMember}
        onRequest="/members"
    />
    <Modal show={showModal}>
        <div slot="modal-body">
            <Input
                bind:value={newMember.first_name} 
                id={"f-name"} 
                title={"First Name"} 
                type={"text"}
            />
            <Input
                bind:value={newMember.last_name} 
                id={"l-name"} 
                title={"Last Name"} 
                type={"text"}
            />
            <Input
                bind:value={newMember.email} 
                id={"email"} 
                title={"Email"} 
                type={"email"}
            />
            <div class="form-group p-2 mb-3">
                <strong>
                    <label for={newMember.permission}>Permission</label>
                </strong>
                <select
                    class="form-select mt-2 input"
                    aria-label={newMember.permission}
                    id={newMember.permission}
                    bind:value={newMember.permission}
                    >
                    {#each Object.entries(memberPermission) as [title, permission] }                        
                        <option class="mt-2 pt-2" value={permission}>{title}</option>
                    {/each}
                </select>
            </div>
            <Alert {showAlert} {message} {_class}/>
        </div>
        <div slot="modal-footer">
            <button type="button" class="btn btn-primary" data-mdb-dismiss="modal"
                on:click={() => (showModal = false)}>
                Close
            </button>
            <button type="button" class="btn btn-success"
                disabled={!validateFields(newMember)}
                on:click={validateAndSubmit}>
                <i class="fas fa-plus"></i> Add
            </button>
        </div>
    </Modal>
    <!-- </Modal> -->
</section>

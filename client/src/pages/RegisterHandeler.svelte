<script>
    import { onMount } from 'svelte';
    import axios from '../healpers/axios'
    import Register from './Register.svelte';
    import InvitationForm from './Invitation.svelte';

    const urlParams = new URLSearchParams(window.location.search);
    const signatureParam = urlParams.has('signature');
    let signature = urlParams.get('signature');
    let data = {}

    if (signatureParam){
        onMount(async () => {
            try {
                const response = await axios.get(`auth/invitation/?signature=${signature}`, data)
            if (response.status === 200) { data = response.data.results }} 
            catch(err) {
                window.location.href = '/not-found'
            }
        });
    }

</script>

{#if signatureParam}
    <InvitationForm data={data}/>
{:else}
    <Register />
{/if}
<script>
    export let objects;
    export let id;
    export let labelTitle;
    export let value;
    export let user=false;
    export let onClick;
</script>

<div class="form-group p-2 mb-3">
    <strong>
        <label for={id}>{labelTitle}</label>
    </strong>
    <select
        class="form-select mt-2 input"
        aria-label={id}
        selected={objects[0]}
        id={id}
        bind:value={value}
        on:change={() => onClick()}
        >
        {#each objects as object }
            {#if user}
                <option value={object.id}>{object.full_name}</option>
            {:else}
                <option value={object.id}>{object.title}</option>
            {/if}
        {/each}
    </select>
</div>
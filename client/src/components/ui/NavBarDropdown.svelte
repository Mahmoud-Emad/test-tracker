<script>
    import { Router, Link } from "svelte-navigator";
</script>


<div class="d-flex align-items-center">
    <div class="dropdown">
        <Router>
            <Link
                class="dropdown-toggle d-flex align-items-center hidden-arrow"
                to="#"
                id="navbarDropdownMenuAvatar"
                role="button"
                data-mdb-toggle="dropdown"
                aria-expanded="false"
                >
                <slot name="dropdown-toggle"></slot>
            </Link>
        </Router>
        <ul
            class="dropdown-menu dropdown-menu-end"
            aria-labelledby="navbarDropdownMenuAvatar"
        >
            <slot name="dropdown-li"></slot>
        </ul>
    </div>
</div>

<svelte:head>
    <style>
        a{
            text-decoration: none !important;
            color: #5a79b1 !important;
        }
    </style>
</svelte:head>
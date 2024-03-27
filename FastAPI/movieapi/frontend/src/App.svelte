<script>
    import Router from "svelte-spa-router";
    import Navigation from "./components/Navigation.svelte";
    import Home from "./routes/Home.svelte";
    import Detail from "./routes/Detail.svelte";
    import UserCreate from "./routes/UserCreate.svelte";

    const routes = {
        "/": Home,
        "/detail": Detail,
        "/user-create": UserCreate,
    };
</script>

<Navigation />
<Router {routes} />

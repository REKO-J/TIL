<script>
    import Router from "svelte-spa-router";
    import Navigation from "./components/Navigation.svelte";
    import Home from "./routes/Home.svelte";
    import Detail from "./routes/Detail.svelte";

    const routes = {
        "/": Home,
        "/detail": Detail,
    };
</script>

<Navigation />
<Router {routes} />

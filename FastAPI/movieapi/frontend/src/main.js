import "./app.css";
import App from "./App.svelte";
// bootstrap
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

const app = new App({
    target: document.getElementById("app"),
});

export default app;

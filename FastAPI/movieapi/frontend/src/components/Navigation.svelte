<script>
    import { movieSearchStore } from "../lib/store.js"; // store 가져오기
    import { link } from "svelte-spa-router";

    let movieSearch = "";

    function searchMovie() {
        // 검색 버튼 클릭 시 movieSearch 값을 스토어에 업데이트
        movieSearchStore.set(movieSearch);
    }

    function handleKeyPress(event) {
        if (event.key === "Enter") {
            searchMovie();
        }
    }

    function Refresh() {
        // 페이지 새로 고침
        location.reload();
    }
</script>

<div class="navigation">
    <div style="font-size: 40px; font-weight: bold; margin: 15px 0px;">
        <a use:link href="/" on:click={Refresh} style="text-decoration: none; color: black;">Movie World</a>
    </div>
    <div style="display: flex; justify-content: space-between;">
        <div class="search-container">
            <input style="width: 300px;" type="text" class="search-box" bind:value={movieSearch} placeholder="영화명으로 검색해보세요." on:keydown={handleKeyPress} />
            <button class="search-button" on:click={searchMovie}><a use:link href="/" style="text-decoration: none; color: black;">검색</a></button>
        </div>
        <div class="box">
            <a use:link href="/user-login" class="box">로그인</a>
            <a use:link href="/user-create" class="box">회원가입</a>
        </div>
    </div>
</div>

<style>
    .navigation {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 0px 200px;
        border-bottom: 2px solid gray;
    }

    .box {
        text-decoration: none;
        color: black;
        display: flex;
        align-items: center;
        font-weight: bold;
        margin: 0px 10px;
    }
</style>

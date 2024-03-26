<script>
    import { movieSearchStore } from "../lib/store.js"; // store 가져오기
    import { movieIndexStore } from "../lib/store.js"; // store 가져오기
    import { link } from "svelte-spa-router";

    // movieSearchStore의 값을 읽어와서 변수에 할당
    let movieSearchValue = "";

    $: {
        movieSearchValue = $movieSearchStore;
        if (movieSearchValue) {
            searchMovie();
            movieData = [];
        }
    }

    let movieData = [];

    async function searchMovie() {
        const response = await fetch(`http://127.0.0.1:8000/fetch_data?title=${movieSearchValue}`);
        const json = await response.json();

        // JSON 데이터를 처리하여 변수에 할당
        movieData = json.Data[0].Result.map((item) => {
            let pattern = /['!HS', '!HE']/g;

            return {
                poster: item.posters.split("|"),
                title: item.title.replace(pattern, " "),
            };
        });
    }

    // 클릭된 movie-container의 index를 저장하는 함수
    function handleClick(index) {
        // 포스터 선택 시 movie_index 값을 스토어에 업데이트
        movieIndexStore.set(index);
    }
</script>

<div class="container">
    {#if movieData == ""}
        <div>검색 결과가 없습니다.</div>
    {:else}
        <div>[{movieSearchValue}] 의 검색 결과입니다.</div>
        <div style="display: flex; margin: 20px 0px; flex-wrap: wrap">
            {#each movieData as movie, index}
                {#if movie.poster[0] == ""}
                    <div class="movie-container">
                        <a use:link href="/detail" on:click={() => handleClick(index)} style="text-decoration: none; color: black;">
                            <img class="poster" src="https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg" alt="" />
                            <div style="margin: 10px 0px;">{movie.title}</div>
                        </a>
                    </div>
                {:else}
                    <div class="movie-container">
                        <a use:link href="/detail" on:click={() => handleClick(index)} style="text-decoration: none; color: black;">
                            <img class="poster" src={movie.poster[0]} alt="" />
                            <div style="margin: 10px 0px;">{movie.title}</div>
                        </a>
                    </div>
                {/if}
            {/each}
        </div>
    {/if}
</div>

<style>
    .container {
        margin: 50px 200px;
    }

    .movie-container {
        width: 250px;
        height: 380px;
        display: flex;
        flex-direction: column;
        text-align: center;
        align-items: center;
    }

    .poster {
        width: 200px;
        height: 300px;
    }
</style>

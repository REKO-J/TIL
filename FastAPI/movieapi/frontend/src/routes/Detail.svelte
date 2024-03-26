<script>
    import { movieSearchStore, movieIndexStore } from "../lib/store.js"; // store 가져오기

    // movieSearchStore의 값을 읽어와서 변수에 할당
    let movieSearchValue = "";
    let movieIndexValue = "";

    $: {
        movieSearchValue = $movieSearchStore;
        movieIndexValue = $movieIndexStore;
        if (movieSearchValue) {
            searchMovie();
        }
    }

    let posters = [];
    let title;
    let prodYear;
    let nation;
    let directorNm;
    let actors = [];
    let plot;

    async function searchMovie() {
        const response = await fetch(`http://127.0.0.1:8000/fetch_data?title=${movieSearchValue}`);
        const json = await response.json();

        // JSON 데이터를 처리하여 변수에 할당
        const movieIndex = parseInt(movieIndexValue); // movieIndexValue를 정수로 변환

        posters = json.Data[0].Result[movieIndex].posters.split("|");
        title = json.Data[0].Result[movieIndex].title.replace("!HS", "").replace("!HE", "").trim();
        prodYear = json.Data[0].Result[movieIndex].prodYear;
        nation = json.Data[0].Result[movieIndex].nation;
        directorNm = json.Data[0].Result[movieIndex].directors.director[0].directorNm;
        actors = json.Data[0].Result[movieIndex].actors.actor.map((actor) => actor.actorNm);
        plot = json.Data[0].Result[movieIndex].plots.plot[0].plotText;
    }
</script>

<div class="container">
    <div class="movie-container">
        <div>
            {#if posters[0] == ""}
                <img class="poster" src="https://t4.ftcdn.net/jpg/04/73/25/49/360_F_473254957_bxG9yf4ly7OBO5I0O5KABlN930GwaMQz.jpg" alt="" />
            {:else}
                <img class="poster" src={posters[0]} alt="" />
            {/if}
        </div>
        <div class="movie-info">
            <div><b>정보</b> {title}ㅣ{prodYear}ㅣ{nation}</div>
            <div><b>감독</b> {directorNm}</div>
            <div><b>출연</b> {actors}</div>
            <div style="height: 20px;"></div>
            <div><b>줄거리</b><br /> {plot}</div>
        </div>
    </div>
</div>

<style>
    .container {
        margin: 50px 200px;
    }

    .movie-container {
        display: flex;
    }

    .poster {
        width: 350px;
        height: 500px;
        margin-right: 30px;
    }

    .movie-info {
        margin-right: 10px;
    }
</style>

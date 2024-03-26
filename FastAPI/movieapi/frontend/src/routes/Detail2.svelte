<script>
    import { movieSearchStore } from "../lib/store.js"; // store 가져오기

    // movieSearchStore의 값을 읽어와서 변수에 할당
    let movieSearchValue = "";

    $: {
        movieSearchValue = $movieSearchStore;
    }

    let posters = [];
    let title;
    let prodYear;
    let nation;
    let directorNm;
    let actors = [];
    let plot;

    async function searchMovie() {
        const response = await fetch(`http://127.0.0.1:8000/fetch_data?title=${movieSearchStoreValue}`);
        const json = await response.json();

        // JSON 데이터를 처리하여 변수에 할당
        posters = json.Data[0].Result[0].posters.split("|");
        title = json.Data[0].Result[0].title.replace("!HS", "").replace("!HE", "").trim();
        prodYear = json.Data[0].Result[0].prodYear;
        nation = json.Data[0].Result[0].nation;
        directorNm = json.Data[0].Result[0].directors.director[0].directorNm;
        actors = json.Data[0].Result[0].actors.actor.map((actor) => actor.actorNm);
        plot = json.Data[0].Result[0].plots.plot[0].plotText;
    }

    searchMovie();
</script>

<div style="display: flex; justify-content: center; align-items: center; margin: 50px 200px;">
    <div><img src={posters[0]} alt="이미지를 불러오지 못했습니다." /></div>
    <div style="margin: 20px;">
        <div><b>정보</b> {title}ㅣ{prodYear}ㅣ{nation}</div>
        <div><b>감독</b> {directorNm}</div>
        <div><b>출연</b> {actors}</div>
        <div style="height: 50px;"></div>
        <div><b>줄거리</b><br /> {plot}</div>
    </div>
</div>

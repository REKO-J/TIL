import { writable } from "svelte/store";

// movieSearch를 저장할 writable store 생성
export const movieSearchStore = writable("");
export const movieIndexStore = writable("");

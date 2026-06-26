const slider = document.getElementById("scrubber");
const stateDiv = document.getElementById("state");

slider.oninput = async () => {

    const timestamp = new Date(Date.now() - slider.value * 1000).toISOString();

    const res = await fetch(`/time/state?timestamp=${timestamp}`);
    const state = await res.json();

    stateDiv.innerText = JSON.stringify(state, null, 2);
};
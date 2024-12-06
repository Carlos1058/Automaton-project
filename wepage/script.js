
const submit_bttn= document.getElementById("submit_bttn");
const text_input= document.getElementById("text");
const answer_out= document.getElementById("answer_out");

submit_bttn.addEventListener("click", function() {
    let text= text_input.value;

    fetch(`http://127.0.0.1:8000/name/${text}`,
        {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            }
        }
    )
    .then((response) => response.json())
    .then((json) => {
        answer_out.value= "";
        answer_out.value= json.output;
    })
});
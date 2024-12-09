
const submit_bttn= document.getElementById("submit_bttn");
const text_input= document.getElementById("input_text");
const answer_out= document.getElementById("answer_out");
const answerContainer= document.getElementById("answer-container");

/* Navegation bar buttons */
isTuringMachine= true;

// Turing Machine Button
document.getElementById("turing-machine").addEventListener("click", function(){
    answerContainer.style.display= "flex";
    isTuringMachine= true;
});
// NFA Button
document.getElementById("nfa").addEventListener("click", function(){
    answerContainer.style.display= "none";
    isTuringMachine= false;
});


submit_bttn.addEventListener("click", function() {
    let text= text_input.value;

    (isTuringMachine) ? console.log("Turing Machine API") : console.log("NFA API");

    if (isTuringMachine)        // Request to the TuringMachine API
    {
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
    }
    else                        // Request to the NFA API
    {

    }
    
});
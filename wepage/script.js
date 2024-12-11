
const submit_bttn= document.getElementById("submit_bttn");
const text_input= document.getElementById("input_text");
const answer_out= document.getElementById("answer_out");
const answerContainer= document.getElementById("answer-container");

/* Navegation bar buttons */
isTuringMachine= true;

// Turing Machine Button
document.getElementById("turing-machine").addEventListener("click", function(element){
    document.getElementById("turing-machine").style.color= "rgb(44, 155, 122)";
    document.getElementById("nfa").style.color= "rgb(255, 255, 255)";
    document.getElementById("turing-machine-header-1").style.display = "block";  
    document.getElementById("nfa-header-1").style.display = "none"; 
    document.getElementById("turing-machine-header-2").style.display = "block";  
    document.getElementById("nfa-header-2").style.display = "none";  
    isTuringMachine= true;
});
// NFA Button
document.getElementById("nfa").addEventListener("click", function(){
    document.getElementById("nfa").style.color= "rgb(44, 155, 122)";
    document.getElementById("turing-machine").style.color= "rgb(255, 255, 255)";
    document.getElementById("nfa-header-1").style.display = "block";  
    document.getElementById("turing-machine-header-1").style.display = "none ";  
    document.getElementById("nfa-header-2").style.display = "block";  
    document.getElementById("turing-machine-header-2").style.display = "none ";  
    isTuringMachine= false;
});


submit_bttn.addEventListener("click", function() {
    let text= text_input.value;

    (isTuringMachine) ? console.log("Turing Machine API") : console.log("NFA API");

    if (isTuringMachine)        // Request to the TuringMachine API
    {
        fetch(`http://127.0.0.1:8000/TuringMachine/true`,
            {
                method: "POST",
                body: JSON.stringify({"cadena":text}),
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
    else                      // Request to the NFA API
    {
        console.log(text);
        fetch(`http://127.0.0.1:8000/NFA/true`,
            {
                method: "POST",
                body: JSON.stringify({"cadena":text}),
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
    
});
function generateExamList(exams) {
    var mainContent = document.getElementById("content");

    exams.forEach((exam) => {
        var card = document.createElement("div");
        // set class name to CSS each card
        card.className = "grid-item";

        var cardBody = document.createElement("div");
        // customize cardBody content
        cardBody.innerHTML = `
            Name: ${exam.name} <br>
            Question ${exam.question} <br>
            Answer: ${exam.answer}
        `;

        card.appendChild(cardBody);
        mainContent.appendChild(card);
    });
}

// use getExams() instead of generateExamList() in dashboard_user.html
// when call API to fetch real data

// function getExams(){
//     fetch(<API>)
//       .then(response => response.json())
//       .then(data => {
//             console.log(data);
//             generateExamList(data);
//       })
// }

generateExamList([
    {
        name: "name1",
        question: "question1",
        answer: "answer1",
    },
    {
        name: "name2",
        question: "question2",
        answer: "answer2",
    },
    {
        name: "name2",
        question: "question2",
        answer: "answer2",
    },
    {
        name: "name2",
        question: "question2",
        answer: "answer2",
    },
    {
        name: "name2",
        question: "question2",
        answer: "answer2",
    },
    {
        name: "name2",
        question: "question2",
        answer: "answer2",
    },
]);

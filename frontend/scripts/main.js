
$(function () {
	const categoriesURL = "http://127.0.0.1:8000/api/categories/";

	$.get(categoriesURL, function (data) {
		$(".container").empty();

		let categories = data.results;

		$.each(categories, function (i, category) {
			let card = `<div class="card category-card" data-id=${category.id} style="--cards: 4">
			<div class="child">
			<h2>${category.name}</h2>
			</div>
			</div>`;

			$(".container").append(card);
		});
	});
});

$("body").on("click", ".category-card", function (event) {
	const categoryQuizzesURL =
		"http://127.0.0.1:8000/api/quizzes/?category_id=";
	const category_id = $(this).data("id");

	$.get(categoryQuizzesURL + category_id, function (data) {
		$(".container").empty();

		let quizzes = data.results;

		$.each(quizzes, function (i, quiz) {
			let card = `<div class="card quiz-card" data-id=${quiz.id} style="--cards: 4">
			<div class="child">
			<h2>${quiz.name}</h2>
			</div>
			</div>`;

			$(".container").append(card);
		});

	});
});

$("body").on("click", ".quiz-card", function (event) {
	const quizQuestionsURL = "http://127.0.0.1:8000/api/quizzes/";
	const quiz_id = $(this).data("id");

	$.get(quizQuestionsURL + quiz_id, function (data) {
		let html = `<h1>${data.name}</h1>`;

		$(".container").empty();

		questions = data.questions;

		html += `<form method="POST" id="quiz-form">`;
		$.each(questions, function (i, question) {
			html += `<div><fieldset><legend>${question.question}</legend>`;
			if (question.type == "text_answer") {
				html += `
						<div>
							<input type="text" name=${question.id}>
						</div>
						`;
			} else if (question.type == "choice") {
				$.each(question.choices, function (i, choice) {
					html += `
					<div>
						<input type="checkbox" name="${question.id}" id="${choice.id}" value="${choice.id}" />
						<label for="${choice.id}">${choice.choice}</label>
					</div>
					`;
				});
			} else if (question.type == "radio") {
				$.each(question.choices, function (i, choice) {
					html += `
					<div>
						<input type="radio" name="${question.id}" id="${choice.id}" value="${choice.id}" />
						<label for="${choice.id}">${choice.choice}</label>
					</div>
					`;
				});
			}

			html += "</fieldset></div>";
		});

		html += `<br><input id="submit-quiz-btn" type="submit" value="Submit">`;
		html += `</form>`;

		$(".common-container").append(html);
	});
});

$("body").on("submit", "#quiz-form", function (event) {
	event.preventDefault();

	inputValues = $("#quiz-form").serializeArray();

	let mark = 0;
	let maxMark = 0;

	$.each(questions, function (i, question) {
		if (question.type == "choice") {
			let choiceMark = 0;
			$.each(inputValues, function (i, inputValue) {
				if (question.id == inputValue.name) {
					$.each(question.choices, function (i, choice) {
						if (inputValue.value == choice.id) {
							if (choice.correct_answer) {
								choiceMark += 1;
							} else {
								choiceMark -= 1;
							}
						}
					});
				}
			});
			if (choiceMark > 0) mark += choiceMark;
		} else if (question.type == "radio") {
			$.each(inputValues, function (i, inputValue) {
				if (question.id == inputValue.name) {
					$.each(question.choices, function (i, choice) {
						if (inputValue.value == choice.id) {
							if (choice.correct_answer) mark += 1;
						}
					});
					return false;
				}
			});
		} else if (question.type == "text_answer") {
			$.each(inputValues, function (i, inputValue) {
				if (question.id == inputValue.name) {
					$.each(question.choices, function (i, choice) {
						if (
							inputValue.value.toLowerCase() ==
							choice.choice.toLowerCase()
						) {
							mark += 1;
						}
					});
					return false;
				}
			});
		}
	});

	$.each(questions, function (i, question) {
		$.each(question.choices, function (i, choice) {
			if (choice.correct_answer) maxMark += 1;
		});
	});

	$(".common-container").empty();
	$(".container").empty();

	html = `<h1>Result: ${mark}\\${maxMark}</h1>
		<br>
		`;

	$(".common-container").append(html);

	console.log(mark);
	console.log(inputValues);
	console.log(questions);
});


$("body").on("click", "#back-home-btn", function (event) {
	location.reload();
})

$("body").on("click", "#login-btn", function (event) {
	$(".common-container").empty();
	$(".container").empty();

	html = `<form id="login-form">
				<input type="text" name="username" placeholder="Your Username">
				<input type="password" name="password" placeholder="Your Password">
				<input type="submit" value="Login">
			</form>
				`

	$(".common-container").append(html);		
})


$("body").on("submit", "#login-form", function (event) {
	event.preventDefault();

	const loginEndpoint = `http://127.0.0.1:8000/api/token/`

	let inputValues = $("#login-form").serialize();

	$.post(loginEndpoint, inputValues,
		function (data) {
			localStorage.setItem('access', data.access)
			localStorage.setItem('refresh', data.refresh)
			
			$(".common-container").empty();
			$(".common-container").append("<h1>Success</h1>");
		}
	)
	.fail(function(){
		$(".common-container").empty();
		$(".common-container").append("<h1>The provided credentials are not valid</h1>");
		
	})

});

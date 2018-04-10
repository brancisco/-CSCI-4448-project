class Poll {
	constructor(name='') {
		this.setName(name);
		this.questions = [];
	}
	getName() {
		return this.name;
	}
	setName(name) {
		this.name = name;
	}
	addQuestion(text) {
		this.questions.push(new Question(text));
		return this.questions.length-1;
	}
	getQuestion(ind) {
		if (ind < this.questions.length)
			return this.questions[ind].getText();
		else
			return null;
	}
	delQuestion(ind) {
		var temp = [];
		for(var i = 0; i < this.questions.length; i ++) {
			if(i != ind) {
				temp.push(this.questions[i]);
			}
		}
		this.questions = temp;
	}
	updateQuestion(ind, text) {
		if (ind < this.questions.length)
			this.questions[ind].setText(text);
	}
	addAnswer(q_ind, text='', correct=false) {
		if (q_ind < this.questions.length)
			this.questions[q_ind].addAnswer(text, correct);
	}
	delAnswer(q_ind, a_ind) {
		if (q_ind < this.questions.length)
			this.questions[q_ind].delAnswer(a_ind);
	}
	updateAnswer(q_ind, a_ind, text, correct=null) {
		if (q_ind < this.questions.length)
			this.questions[q_ind].updateAnswer(a_ind, text, correct);
	}
	setCorrect(q_ind, a_ind) {
		if (q_ind < this.questions.length)
			this.questions[q_ind].setCorrect(a_ind);
	}
	getCorrect() {
		var status = [];
		for(var i = 0; i < this.questions.length; i ++) {
			status.push(this.questions[i].getCorrect());
		}
		return status;
	}
	getAnswers(q_ind) {
		return this.questions[q_ind].getAnswers();
	}
}

class TextInterface {

	constructor(text='') {
		this.text = '';
		this.setText(text);
	}
	getText() {
		return this.text;
	}
	setText(text) {
		this.text = text;
	}
}

class Question extends TextInterface {
	constructor(text='') {
		super(text);
		this.answers = [];
	}
	addAnswer(text, correct=false) {
		this.answers.push(new Answer(text));
		if(correct) {
			this.setCorrect(this.answers.length-1);
		}
	}
	delAnswer(ind) {
		var temp = [];
		for(var i = 0; i < this.answers.length; i ++) {
			if(i != ind) {
				temp.push(this.answers[i]);
			}
		}
		this.answers = temp;
	}
	updateAnswer(ind, text, correct=null) {
		if(ind < this.answers.length) {
			this.answers[ind].setText(text);
			if(correct !== null && correct === true) {
				this.setCorrect(ind);
			}
		}
	}
	getCorrect() {
		for(var i = 0; i < this.answers.length; i ++) {
			if(this.answers[i].getCorrect()) {
				return i;
			}
		}
	}
	setCorrect(ind) {
		for(var i = 0; i < this.answers.length; i ++) {
			if(i == ind)
				this.answers[i].setCorrect(true);
			else 
				this.answers[i].setCorrect(false)
		}
	}
	getAnswer() {
		for(var i = 0; i < this.answers.length; i ++) {
			if(this.answers[i].getCorrect()) {
				return this.answers[i].getText();
			}
		}
	}
	getAnswers() {
		var answers = [];
		for(var i = 0; i < this.answers.length; i ++) {
			answers.push(this.answers[i].getText());
		}
		return answers;
	}
}

class Answer extends TextInterface {
	
	constructor(text='', correct=false) {
		super(text);
		this.setCorrect(correct);
	}
	setCorrect(correct) {
		this.correct = correct;
	}
	getCorrect() {
		return this.correct;
	}
}

// var poll = new Poll('cool poll');
// poll.addQuestion('Question # 1');
// poll.addQuestion('Question # 2');
// poll.addQuestion('Question # 3');
// poll.addQuestion('Question # 4');
// poll.addQuestion('Question # 5');

// for(var i = 0; i < poll.questions.length; i ++) {
// 	poll.addAnswer(i, 'bad');
// 	poll.addAnswer(i, 'good');
// 	poll.addAnswer(i, 'great');
// 	var ind = Math.random();
// 	ind = (ind < 0.3? 0: (ind < 0.6? 1: 2))
// 	poll.setCorrect(i, ind)
// }
// console.log(poll);
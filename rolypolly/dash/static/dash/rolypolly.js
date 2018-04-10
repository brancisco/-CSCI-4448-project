class Poll {
	constructor(name='') {
		this.setName(name);
	}
	getName() {
		return this.name;
	}
	setName(name) {
		this.name = name;
	}
}

class TextInterface {

	constructor(text='') {
		this.text = '';
		this.setText(text)
	}
	getText() {
		return this.text;
	}
	setText(text) {
		this.text = text;
	}
}

class Question extends TextInterface {
	
}

class Answer extends TextInterface {
	
}


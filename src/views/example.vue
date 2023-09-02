<template>
  <div>
    <h2>Тренажер слепой печати</h2>
    <div class="text-container">
      <p>
        <span
            v-for="(char, index) in currentText"
            :key="index"
            :class="{
            'correct': index < activeChar,
            'incorrect': index === activeChar,
            'delete-animation': index === activeChar - 1 && isIncorrect
          }"
        >
          {{ char }}
        </span>
      </p>
    </div>
    <input
        type="text"
        v-model="userInput"
        @input="checkInput"
        :disabled="!isActive"
        ref="inputField"
        :class="{ 'incorrect-input': isIncorrect }"
        :style="{ 'border-color': activeChar === currentText.length ? (userInput === currentText ? 'green' : 'red') : '' }"
        @keydown="disableDelete"
        autofocus
    />
    <div v-if="showResults">
      <p>
        Завершено: {{ completed }} из {{ total }} символов.
      </p>
      <p>
        Точность: {{ accuracy }}%
      </p>
      <p>
        Скорость печати: {{ typingSpeed }} символов в минуту.
      </p>
    </div>
    <button @click="start" :disabled="isActive">Начать</button>
    <button @click="reset">Сбросить</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: 'Текст для тренировки слепой печати.',
      currentText: '',
      userInput: '',
      activeChar: 0,
      completed: 0,
      total: 0,
      startTime: null,
      endTime: null,
      showResults: false,
      isActive: false,
      isIncorrect: false,
    };
  },
  computed: {
    accuracy() {
      if (this.completed > 0) {
        return ((this.completed / this.total) * 100).toFixed(2);
      }
      return 0;
    },
    typingSpeed() {
      if (this.startTime && this.endTime) {
        const totalTime = (this.endTime - this.startTime) / 1000; // в секундах
        const speed = (this.completed / totalTime) * 60; // символов в минуту
        return speed.toFixed(2);
      }
      return 0;
    },
  },
  methods: {
    start() {
      this.isActive = true;
      this.total = this.text.length;
      this.currentText = this.text;
      this.startTime = new Date();
      this.$nextTick(() => {
        this.$refs.inputField.focus();
      });
    },
    checkInput() {
      const enteredChar = this.userInput.charAt(this.activeChar);

      if (enteredChar === this.currentText.charAt(this.activeChar)) {
        this.completed++;
        this.activeChar++;

        if (this.activeChar === this.total) {
          this.endTime = new Date();
          this.isActive = false;
          this.showResults = true;
        }
      } else {
        this.isIncorrect = true;
        setTimeout(() => {
          this.isIncorrect = false;
          this.userInput = this.userInput.slice(0, this.activeChar);
        }, 500);
      }
    },
    disableDelete(event) {
      if (event.keyCode === 8 && this.activeChar > 0) {
        event.preventDefault();
      }
    },
    reset() {
      this.activeChar = 0;
      this.completed = 0;
      this.total = 0;
      this.startTime = null;
      this.endTime = null;
      this.showResults = false;
      this.isActive = false;
      this.currentText = '';
      this.userInput = '';
      this.isIncorrect = false;
    },
  },
};
</script>

<style>
.text-container {
  margin-bottom: 10px;
}

.correct {
  color: black;
}

.incorrect {
  color: red;
}

.delete-animation {
  animation: deleteCharAnimation 0.5s linear;
}

.incorrect-input {
  color: red;
}

input[type="text"] {
  padding: 5px;
  width: 100%;
}

@keyframes deleteCharAnimation {
  0% {
    opacity: 1;
    transform: scale(1);
  }
  100% {
    opacity: 0;
    transform: scale(0);
  }
}
</style>
<template>
  <div class="main-wrapper">
    <template v-if="!this.$store.state.isTaskDone">
      <div  class="main-info">
        <div class="main-info__quantity-block">
          <div class="quentity-block__wrapper">
            <span :class="{'blue': this.$store.state.selectLang === 'C++'}" class="quentity-block__text">{{correctLengthChar}}</span>
            <span :class="{'blue': this.$store.state.selectLang === 'C++'}" class="quentity-block__text">/</span>
            <span :class="{'blue': this.$store.state.selectLang === 'C++'}" class="quentity-block__text">{{this.currentTask.length}}</span>
          </div>
          <button @click="nextTask" class="main-info__restart">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="29"
                height="29"
                viewBox="0 0 29 29"
                fill="none"
                class="restart-img"
                :class="{'blue': this.$store.state.selectLang}">
              <path class="restart-img" :class="{'blue': this.$store.state.selectLang === 'C++'}" d="M14.2502 2.50012C17.1399 2.50017 19.9365 3.52177 22.1458 5.38437C24.3551 7.24696 25.8349 9.83063 26.3235 12.6787C26.8121 15.5268 26.2782 18.4559 24.816 20.9484C23.3538 23.4409 21.0576 25.3362 18.3332 26.2994C15.6087 27.2627 12.6315 27.2317 9.92765 26.2121C7.22381 25.1925 4.96747 23.2499 3.55741 20.7275C2.14735 18.2052 1.67437 15.2656 2.22206 12.4283C2.76975 9.59098 4.30285 7.03862 6.55039 5.22233" stroke="#FEB81C" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              <path class="restart-img" :class="{'blue': this.$store.state.selectLang === 'C++'}" d="M2.00012 4.54187H7.44454V9.98629" stroke="#FEB81C" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>
        </div>
        <div class="main-info__timer" :class="{'blue': this.$store.state.selectLang === 'C++'}">
          <span class="main-info__timer__text" :class="{'blue': this.$store.state.selectLang === 'C++'}" >{{timeTask}}</span>
        </div>
        <div class="main-info__right">
          <div class="main-info__select">
            <button class="main-info__select__control" @click="isSelectedActive = !isSelectedActive">
              <img :src="this.selectLang.icon" alt="Selected Language Icon">
              <svg class="main-info__select__arrow" xmlns="http://www.w3.org/2000/svg" width="24" height="25" viewBox="0 0 24 25" fill="none">
                <path :class="{'blue': this.$store.state.selectLang === 'C++'}" d="M7 9.5L12 14.5L17 9.5" stroke="#FEB81C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
            <div  class="main-info__select__list" :class="{active: isSelectedActive, 'blue': this.$store.state.selectLang === 'C++'}">
              <p class="main-info__select-item" :class="{'blue': this.$store.state.selectLang === 'C++'}" v-for="lang of languages" :key='lang.lang' @click="selectedLang(lang.lang)">{{lang.lang}}</p>
            </div>
          </div>
        </div>
      </div>
      <p class="main-task__code">
      <span
          class="main-task__char"
          v-for="(char, index) in this.currentTask"
          :key="index"
          :class="{
            'correct': index < activeChar,
            'current': index === activeChar,
            'incorrect': index === IncorrectChar,
            'blue': this.$store.state.selectLang === 'C++'
          }"
      >{{char}}</span>
      </p>
      <div class="main-task">
        <input
            type="text"
            class="main-task__input"
            v-model="this.userInput"
            @input="checkInput"
            @keydown="handlerKey"
            :class="{'blue': this.$store.state.selectLang === 'C++'}"
            autofocus
            placeholder="your answer...">
      </div>
    </template>
      <template v-else>
        <div class="main__wrapper-statistics">
          <div class="statistics-top" :class="{'blue': this.$store.state.selectLang === 'C++'}">
            <h2
                class="statistics-top__title"
                :class="{'blue': this.$store.state.selectLang === 'C++'}">Statistic</h2>
          </div>
          <div class="statistics-info">
            <div class="statistics-info__block">
              <svg class="statistics-info__block__img" xmlns="http://www.w3.org/2000/svg" width="50" height="57" viewBox="0 0 50 57" fill="none">
                <path :class="{'blue': this.$store.state.selectLang === 'C++'}"  d="M24.985 7.44536C31.4281 7.44536 37.6074 10.0049 42.1635 14.5609C46.7195 19.1169 49.279 25.2962 49.279 31.7394C49.279 38.1826 46.7195 44.3619 42.1635 48.9179C37.6074 53.4739 31.4281 56.0334 24.985 56.0334C18.5418 56.0334 12.3625 53.4739 7.80648 48.9179C3.25046 44.3619 0.690918 38.1826 0.690918 31.7394C0.690918 25.2962 3.25046 19.1169 7.80648 14.5609C12.3625 10.0049 18.5418 7.44536 24.985 7.44536ZM24.985 11.7325C19.6788 11.7325 14.59 13.8404 10.838 17.5924C7.08596 21.3444 4.9781 26.4333 4.9781 31.7394C4.9781 37.0456 7.08596 42.1344 10.838 45.8864C14.59 49.6384 19.6788 51.7463 24.985 51.7463C30.2911 51.7463 35.3799 49.6384 39.132 45.8864C42.884 42.1344 44.9918 37.0456 44.9918 31.7394C44.9918 26.4333 42.884 21.3444 39.132 17.5924C35.3799 13.8404 30.2911 11.7325 24.985 11.7325ZM24.985 16.0197C25.503 16.0197 26.0034 16.2073 26.3938 16.5478C26.7842 16.8883 27.0381 17.3586 27.1086 17.8718L27.1286 18.1633V31.0249C27.1284 31.568 26.9221 32.0908 26.5513 32.4876C26.1805 32.8845 25.6729 33.1258 25.1311 33.1628C24.5892 33.1998 24.0535 33.0298 23.6322 32.6871C23.2109 32.3443 22.9354 31.8544 22.8614 31.3164L22.8414 31.0249V18.1633C22.8414 17.5948 23.0672 17.0496 23.4692 16.6476C23.8712 16.2456 24.4165 16.0197 24.985 16.0197ZM45.412 7.77118L45.6492 7.94267L48.9589 10.6979C49.3733 11.0464 49.6405 11.5389 49.7067 12.0763C49.7729 12.6138 49.6333 13.1564 49.3158 13.5951C48.9984 14.0338 48.5267 14.3361 47.9955 14.4412C47.4643 14.5464 46.913 14.4466 46.4523 14.1619L46.218 13.9905L42.9054 11.2352C42.491 10.8867 42.2238 10.3942 42.1576 9.85679C42.0914 9.31935 42.2311 8.77677 42.5485 8.33807C42.8659 7.89938 43.3376 7.59708 43.8688 7.49192C44.4 7.38675 44.9513 7.48653 45.412 7.77118ZM31.4157 0.300049C31.9589 0.300215 32.4817 0.506533 32.8785 0.877312C33.2754 1.24809 33.5167 1.75569 33.5537 2.29753C33.5907 2.83938 33.4207 3.37508 33.0779 3.79639C32.7352 4.21769 32.2453 4.4932 31.7073 4.56723L31.4157 4.58723H18.5542C18.0111 4.58707 17.4883 4.38075 17.0914 4.00997C16.6946 3.63919 16.4533 3.1316 16.4162 2.58975C16.3792 2.0479 16.5493 1.5122 16.892 1.09089C17.2347 0.669588 17.7246 0.394085 18.2627 0.320056L18.5542 0.300049H31.4157Z" fill="#FEB81C"/>
              </svg>
              <div class="statistics-info__block__info">
                <p class="statistics-info__block__value">30</p>
                <p
                    class="statistics-info__block__description"
                   :class="{'blue': this.$store.state.selectLang === 'C++'}">Time</p>
              </div>
            </div>
            <div class="statistics-info__block">
              <svg class="statistics-info__block__img" xmlns="http://www.w3.org/2000/svg" width="64" height="65" viewBox="0 0 64 65" fill="none">
                <path :class="{'blue': this.$store.state.selectLang === 'C++'}" d="M32 56.5C35.1517 56.5 38.2726 55.8792 41.1844 54.6731C44.0962 53.467 46.742 51.6992 48.9706 49.4706C51.1992 47.242 52.967 44.5962 54.1731 41.6844C55.3792 38.7726 56 35.6517 56 32.5C56 29.3483 55.3792 26.2274 54.1731 23.3156C52.967 20.4038 51.1992 17.758 48.9706 15.5294C46.742 13.3008 44.0962 11.533 41.1844 10.3269C38.2726 9.12078 35.1517 8.5 32 8.5C25.6348 8.5 19.5303 11.0286 15.0294 15.5294C10.5286 20.0303 8 26.1348 8 32.5C8 38.8652 10.5286 44.9697 15.0294 49.4706C19.5303 53.9714 25.6348 56.5 32 56.5ZM32 60.5C24.5739 60.5 17.452 57.55 12.201 52.299C6.94999 47.048 4 39.9261 4 32.5C4 25.0739 6.94999 17.952 12.201 12.701C17.452 7.44999 24.5739 4.5 32 4.5C39.4261 4.5 46.548 7.44999 51.799 12.701C57.05 17.952 60 25.0739 60 32.5C60 39.9261 57.05 47.048 51.799 52.299C46.548 57.55 39.4261 60.5 32 60.5Z" fill="#FEB81C"/>
                <path :class="{'blue': this.$store.state.selectLang === 'C++'}" d="M32 6.5C32.5304 6.5 33.0391 6.71071 33.4142 7.08579C33.7893 7.46086 34 7.96957 34 8.5V20.5C34 21.0304 33.7893 21.5391 33.4142 21.9142C33.0391 22.2893 32.5304 22.5 32 22.5C31.4696 22.5 30.9609 22.2893 30.5858 21.9142C30.2107 21.5391 30 21.0304 30 20.5V8.5C30 7.96957 30.2107 7.46086 30.5858 7.08579C30.9609 6.71071 31.4696 6.5 32 6.5ZM32 42.5C32.5304 42.5 33.0391 42.7107 33.4142 43.0858C33.7893 43.4609 34 43.9696 34 44.5V56.5C34 57.0304 33.7893 57.5391 33.4142 57.9142C33.0391 58.2893 32.5304 58.5 32 58.5C31.4696 58.5 30.9609 58.2893 30.5858 57.9142C30.2107 57.5391 30 57.0304 30 56.5V44.5C30 43.9696 30.2107 43.4609 30.5858 43.0858C30.9609 42.7107 31.4696 42.5 32 42.5ZM6 32.5C6 31.9696 6.21071 31.4609 6.58579 31.0858C6.96086 30.7107 7.46957 30.5 8 30.5H20C20.5304 30.5 21.0391 30.7107 21.4142 31.0858C21.7893 31.4609 22 31.9696 22 32.5C22 33.0304 21.7893 33.5391 21.4142 33.9142C21.0391 34.2893 20.5304 34.5 20 34.5H8C7.46957 34.5 6.96086 34.2893 6.58579 33.9142C6.21071 33.5391 6 33.0304 6 32.5ZM42 32.5C42 31.9696 42.2107 31.4609 42.5858 31.0858C42.9609 30.7107 43.4696 30.5 44 30.5H56C56.5304 30.5 57.0391 30.7107 57.4142 31.0858C57.7893 31.4609 58 31.9696 58 32.5C58 33.0304 57.7893 33.5391 57.4142 33.9142C57.0391 34.2893 56.5304 34.5 56 34.5H44C43.4696 34.5 42.9609 34.2893 42.5858 33.9142C42.2107 33.5391 42 33.0304 42 32.5Z" fill="#FEB81C"/>
              </svg>
              <div class="statistics-info__block__info">
                <p class="statistics-info__block__value">{{this.accuracy}}%</p>
                <p
                    class="statistics-info__block__description"
                    :class="{'blue': this.$store.state.selectLang === 'C++'}">Accuracy</p>
              </div>
            </div>
            <div class="statistics-info__block">
              <svg class="statistics-info__block__img" xmlns="http://www.w3.org/2000/svg" width="64" height="65" viewBox="0 0 64 65" fill="none">
                <g clip-path="url(#clip0_229_34)">
                  <path :class="{'blue-stroke': this.$store.state.selectLang === 'C++'}" d="M33.7321 13.5L35.4641 12.5C33.9245 9.83334 30.0755 9.83332 28.5359 12.5L6.88526 50C5.34566 52.6667 7.27015 56 10.3494 56H53.6506C56.7298 56 58.6543 52.6667 57.1147 50L35.4641 12.5L33.7321 13.5Z" stroke="#FEB81C" stroke-width="4"/>
                  <path :class="{'blue': this.$store.state.selectLang === 'C++'}" d="M32.4546 25.2273C33.3047 25.2273 33.9906 25.9226 33.9791 26.7726L33.7907 40.6365C33.7808 41.3673 33.1855 41.9546 32.4546 41.9546C31.7237 41.9546 31.1285 41.3673 31.1185 40.6365L30.9302 26.7726C30.9186 25.9226 31.6045 25.2273 32.4546 25.2273ZM32.4546 48.6818C31.894 48.6818 31.413 48.4811 31.0115 48.0796C30.6099 47.6781 30.4092 47.197 30.4092 46.6364C30.4092 46.0758 30.6099 45.5947 31.0115 45.1932C31.413 44.7917 31.894 44.5909 32.4546 44.5909C33.0152 44.5909 33.4963 44.7917 33.8978 45.1932C34.2993 45.5947 34.5001 46.0758 34.5001 46.6364C34.5001 47.0076 34.4054 47.3485 34.216 47.6591C34.0342 47.9697 33.788 48.2197 33.4774 48.4091C33.1743 48.5909 32.8334 48.6818 32.4546 48.6818Z" fill="#FEB81C"/>
                </g>
                <defs>
                  <clipPath id="clip0_229_34">
                    <rect width="64" height="64" fill="white" transform="translate(0 0.5)"/>
                  </clipPath>
                </defs>
              </svg>
              <div class="statistics-info__block__info">
                <p class="statistics-info__block__value">{{this.errorInput}}</p>
                <p
                    class="statistics-info__block__description"
                    :class="{'blue': this.$store.state.selectLang === 'C++'}">Error</p>
              </div>
            </div>
            <div class="statistics-info__block">
              <svg class="statistics-info__block__img" xmlns="http://www.w3.org/2000/svg" width="64" height="65" viewBox="0 0 64 65" fill="none">
                <path :class="{'blue-stroke': this.$store.state.selectLang === 'C++'}" d="M15.0293 52.1373C11.6729 48.7809 9.38716 44.5045 8.46114 39.8489C7.53512 35.1934 8.01042 30.3678 9.82693 25.9824C11.6434 21.597 14.7196 17.8487 18.6664 15.2116C22.6131 12.5744 27.2533 11.1669 32 11.1669C36.7468 11.1669 41.3869 12.5744 45.3337 15.2116C49.2804 17.8487 52.3566 21.597 54.1731 25.9824C55.9896 30.3678 56.4649 35.1934 55.5389 39.8489C54.6129 44.5045 52.3271 48.7809 48.9707 52.1373M42.6667 24.5L32 35.1667" stroke="#FEB81C" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              <div class="statistics-info__block__info">
                <p class="statistics-info__block__value">{{this.charPerMinute}}</p>
                <p
                    class="statistics-info__block__description"
                    :class="{'blue': this.$store.state.selectLang === 'C++'}">char/min</p>
              </div>
            </div>
          </div>
          <div class="statistics-bottom">
            <button @click="nextTask" class="statistics-bottom__button">
              <svg
                  class="statistics-bottom__img"
                  xmlns="http://www.w3.org/2000/svg" width="26" height="27" viewBox="0 0 26 27" fill="none">
                <path
                    :class="{'blue-fill': this.$store.state.selectLang === 'C++'}"
                    d="M5.41666 2.1959L22.9427 11.5848C25.1228 12.7528 25.0326 15.9088 22.7894 16.9503L5.26333 25.0874C3.27489 26.0106 1 24.5587 1 22.3664V4.84034C1 2.57313 3.41817 1.12528 5.41666 2.1959Z" fill="#FEB81C" stroke="#FEB81C" stroke-width="2" stroke-linecap="round"/>
              </svg>
            </button>
            <button @click="restartTask" class="statistics-bottom__button">
              <svg
                  class="statistics-bottom__img"
                  xmlns="http://www.w3.org/2000/svg" width="29" height="29" viewBox="0 0 29 29" fill="none">
                <path
                    :class="{'blue': this.$store.state.selectLang === 'C++'}"
                    d="M14.2502 2.50012C17.1399 2.50017 19.9365 3.52177 22.1458 5.38437C24.3551 7.24696 25.8349 9.83063 26.3235 12.6787C26.8121 15.5268 26.2782 18.4559 24.816 20.9484C23.3538 23.4409 21.0576 25.3362 18.3332 26.2994C15.6087 27.2627 12.6315 27.2317 9.92765 26.2121C7.22381 25.1925 4.96747 23.2499 3.55741 20.7275C2.14735 18.2052 1.67437 15.2656 2.22206 12.4283C2.76975 9.59098 4.30285 7.03862 6.55039 5.22233" stroke="#FEB81C" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
                <path
                    :class="{'blue': this.$store.state.selectLang === 'C++'}"
                    d="M2.00012 4.54187H7.44454V9.98629" stroke="#FEB81C" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
          </div>
        </div>
      </template>
  </div>
</template>

<script>
export default {
  name: 'main-content',
  data() {
    return {
      test: false,
      isTaskDone: false,
      isRestartTask: false,
      task: 0,
      timeTask: 30,
      isTimerStart: false,


      selectLang: this.$store.state.languages[0],
      isSelectedActive: false,

      inputChar: 0,
      IncorrectChar: null,
      userInput: '',
      activeChar: 0,
      correctLengthChar: 0,
      errorInput: 0,
      taskJs: this.$store.state.taskJs,
      listT: null,

      currentTask: '',
    }
  },
  methods: {
    selectedLang(lang) {
      const selectLang = this.languages.find(item => item.lang === lang)
      if(selectLang.lang === this.selectLang.lang) {
        return;
      } else {
        this.selectLang = selectLang
        localStorage.setItem('selectLang', JSON.stringify(this.selectLang))
        this.$store.commit('updateSelectLang', this.selectLang.lang)
        this.updateRandomWord()
      }
      // this.selectLang = this.languages.find(item => item.lang === lang)
    },
    updateRandomWord() {
      this.currentTask = this.listTask[Math.floor(Math.random() * this.listTask.length)];
    },
    startTimer() {
      const updateTimer = () => {
        if(this.isRestartTask) {
          return
        }
        if (this.timeTask > 0) {
          this.timeTask--;
          setTimeout(updateTimer, 1000);
        } else {
          this.$store.commit('updateTaskStatus', true)
        }
      };

      this.isTimerStart = true;
      updateTimer();
    },

    checkInput(event) {
      this.inputChar++

      if(!this.isTimerStart) {
        this.isTimerStart = true
        this.isRestartTask = false
        this.isSelectedActive = false
        this.startTimer()
      }

      const enteredChar = this.userInput.charAt(this.activeChar)

      if(enteredChar === this.currentTask.charAt(this.activeChar)) {
        this.IncorrectChar = null
        this.activeChar++
        this.correctLengthChar++

        if(this.correctLengthChar === this.currentTask.length) {
          this.$store.commit('updateTaskStatus', true)
        }
      } else {
        this.IncorrectChar = this.activeChar
        this.errorInput++
      }
    },
    handlerKey(event) {
      if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
        event.preventDefault();
      }
    },
    restartTask() {
      this.$store.commit('updateTaskStatus', false)
      this.isRestartTask = true
      this.userInput = '';
      this.inputChar = 0;
      this.activeChar = 0;
      this.correctLengthChar = 0;
      this.IncorrectChar = null;
      this.errorInput = 0;
      this.timeTask = 30;
      this.isTimerStart = false

    },
    nextTask() {
      this.updateRandomWord();
      this.$store.commit('updateTaskStatus', false);
      this.isRestartTask = true
      this.userInput = '';
      this.inputChar = 0;
      this.activeChar = 0;
      this.correctLengthChar = 0;
      this.IncorrectChar = null,
      this.errorInput = 0;
      this.timeTask = 30;
      this.isTimerStart = false
    },
  },
  computed: {
    languages() {
      return this.$store.state.languages
    },
    listTask() {
      return this.selectLang.task
    },
    accuracy() {
      return ((this.correctLengthChar / this.inputChar) * 100).toFixed(0)
    },
    charPerMinute() {
      return ((this.correctLengthChar / 60) * 100).toFixed(0)
    },
  },
  beforeMount() {
    for(let key in localStorage) {
      if(key === 'selectLang') {
        this.selectLang = JSON.parse(localStorage.getItem('selectLang'))
        this.$store.commit('updateSelectLang', this.selectLang.lang)
      }
    }
    this.listTask = this.selectLang.task
  },
  mounted() {
    this.updateRandomWord()
  },
}
</script>

<style src="@/style/main-content.scss" lang="scss" scoped>

</style>
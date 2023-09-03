<template>
  <div v-if="this.$store.state.isModalVis" class="modal-win-wrapper" @click="closeModal">
    <form class="modal-win">
      <p class="modal-win__title">Registration</p>
      <div class="modal-win__block">
        <input
            v-model.trim="userName"
            @focus="isInputFocusName = true"
            @blur="isInputFocusName = false"
            @keyup="checkName"
            type="text"
            class="modal-win__block__input">
        <span
            class="modal-win__block__placeholder"
            :class="{active: isInputFocusName || userName !== ''}">
        name
        </span>
        <svg v-if="isCheckName === true" class="modal-win-check" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
          <path  d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z"/>
        </svg>
        <svg v-if="isCheckName === false" class="modal-win-check error" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
          <path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"/>
        </svg>
      </div>
      <div class="modal-win__block">
        <input
            v-model.trim="userPassword"
            @focus="isInputFocusPass = true"
            @blur="isInputFocusPass = false; checkPass()"
            type="password"
            class="modal-win__block__input">
        <span
            class="modal-win__block__placeholder"
            :class="{active: isInputFocusPass || userPassword !== ''}">
        password
        </span>
        <svg v-if="isValidPassword === true" class="modal-win-check" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
          <path  d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z"/>
        </svg>
        <svg v-if="isValidPassword === false" class="modal-win-check error" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
          <path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"/>
        </svg>
      </div>
      <div class="modal-win__block">
        <input
            v-model.trim="verifiedPassword"
            @focus="isInputFocusVerPass = true"
            @blur="isInputFocusVerPass = false;"
            @keyup="checkVerifiedPass()"
            type="password"
            class="modal-win__block__input">
        <span
            class="modal-win__block__placeholder"
            :class="{active: isInputFocusVerPass || verifiedPassword !== ''}">
      verified password
      </span>
      <svg v-if="isCheckPass === true" class="modal-win-check" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
        <path  d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z"/>
      </svg>
      <svg v-if="isCheckPass === false" class="modal-win-check error" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
        <path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"/>
      </svg>
      </div>
      <button @click="submitForm" type="submit" class="modal-win__block__btn">submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'the-modal-win',
  data() {
    return {
      showModal: true,

      userName: '',
      isCheckName: null,
      isInputFocusName: false,

      userPassword: '',
      isCheckFieldPass: null,
      isInputFocusPass: false,
      isCheckPass: null,

      verifiedPassword: '',
      isInputFocusVerPass: false,
      isValidPassword: null,

    }
  },
  methods: {
    submitForm() {
      if( !this.isValidPassword || !this.isCheckPass) {
        alert('Error!')
      } else {
        this.$store.commit('updateModalStatus', false)
        this.$store.state.userPassword = this.userPassword
        localStorage.setItem('username', this.userName)
        localStorage.setItem('password', this.userPassword)
        this.userName = '';
        this.userPassword = '';
        this.verifiedPassword = '';
        this.isCheckFieldPass = null;
        this.isCheckName = null;
        this.isCheckPass = null;
        this.isValidPassword = null;
      }
    },
    closeModal(event) {
      if (!event.target.closest('.modal-win')) {
        this.$store.commit('updateModalStatus', false)
      }
    },
    checkName() {
      this.userName !== '' ? this.isCheckName = true : this.isCheckName = false
    },
    checkPass() {
      if(this.userPassword !== '') {
        return this.userPassword.length >= 8 ? this.isValidPassword = true : this.isValidPassword = false
      } else {
      }
    },
    checkVerifiedPass() {
      this.userPassword !== this.verifiedPassword ? this.isCheckPass = false : this.isCheckPass = true
    }
  },
}
</script>

<style src="@/style/modal-window.scss" lang="scss" scoped>

</style>
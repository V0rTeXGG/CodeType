<template>
  <div v-if="this.$store.state.isModalVis" class="modal-win-wrapper" @click="closeModal">
    <form class="modal-win">
      <p class="modal-win__title">Registration</p>
      <div class="modal-win__block">
        <input
            v-model.trim="this.userName"
            @focus="inputFocusLog = true"
            @blur="inputFocusLog = false"
            type="text"
            class="modal-win__block__input">
        <span
            class="modal-win__block__placeholder"
            :class="{active: inputFocusLog || userName !== ''}">
      login
    </span>
      </div>
      <div class="modal-win__block">
        <input
            v-model.trim="this.userPassword"
            @focus="inputFocusPass = true"
            @blur="inputFocusPass = false"
            type="text"
            class="modal-win__block__input">
        <span
            class="modal-win__block__placeholder"
            :class="{active: inputFocusPass || userPassword !== ''}">
      password
    </span>
      </div>
      <button @click="submitForm" type="button" class="modal-win__block__btn">submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'the-modal-win',
  data() {
    return {
      userName: '',
      userPassword: '',
      inputFocusLog: false,
      inputFocusPass: false,
      showModal: true,
    }
  },
  methods: {
    submitForm() {
      if(!this.validName || !this.validPassword) {
        alert('Error!')
      } else {
        localStorage.setItem('username', this.userName)
        localStorage.setItem('password', this.userPassword)
      }
    },
    closeModal(event) {
      if (!event.target.closest('.modal-win')) {
        this.$store.commit('updateModalStatus', false)
      }
    },
  },
  computed: {
    validName() {
      return this.userName !== '' ? true : false
    },
    validPassword() {
     return this.userPassword !== '' && this.userPassword.length >= 8 ? true : false
    }
  }
}
</script>

<style src="@/style/modal-window.scss" lang="scss" scoped>

</style>
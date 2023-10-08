<template>
  <div v-if="this.$store.state.isModalVis" class="modal-win-wrapper" @click="closeModal">
      <form class="modal-win">
        <template v-if="!ModalEnter">
          <p
              class="modal-win__title"
              :class="{'blue': this.$store.state.selectLang === 'C++'}">Registration</p>
          <div class="modal-win__block">
            <input
                v-model.trim="userData.username"
                @focus="isInputFocusName = true;"
                @blur="isInputFocusName = false"
                @keyup="checkName"
                type="text"
                class="modal-win__block__input"
                :class="{'blue': this.$store.state.selectLang === 'C++'}">
            <span
                class="modal-win__block__placeholder"
                :class="{active: isInputFocusName || userData.username !== ''}">
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
                v-model.trim="userData.email"
                @focus="isInputFocusEmail = true;"
                @blur="isInputFocusEmail = false"
                @keyup="checkEmail"
                type="text"
                class="modal-win__block__input"
                :class="{'blue': this.$store.state.selectLang === 'C++'}">
            <span
                class="modal-win__block__placeholder"
                :class="{active: isInputFocusEmail || userData.email !== ''}">
            email
            </span>
            <svg v-if="isCheckEmail=== true" class="modal-win-check" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
              <path  d="M438.6 105.4c12.5 12.5 12.5 32.8 0 45.3l-256 256c-12.5 12.5-32.8 12.5-45.3 0l-128-128c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0L160 338.7 393.4 105.4c12.5-12.5 32.8-12.5 45.3 0z"/>
            </svg>
            <svg v-if="isCheckEmail === false" class="modal-win-check error" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
              <path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"/>
            </svg>
          </div>
          <div class="modal-win__block">
            <input
                v-model.trim="userData.password"
                @focus="isInputFocusPass = true"
                @blur="isInputFocusPass = false; checkPass()"
                type="password"
                class="modal-win__block__input"
                :class="{'blue': this.$store.state.selectLang === 'C++'}">
            <span
                class="modal-win__block__placeholder"
                :class="{active: isInputFocusPass || userData.password !== ''}">
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
                class="modal-win__block__input"
                :class="{'blue': this.$store.state.selectLang === 'C++'}">
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
          <button
              type="submit"
              class="modal-win__block__btn"
              @click.prevent="submitForm">submit</button>
          <button
              type="button"
              class="modal-win__block__enter"
              :class="{'blue': this.$store.state.selectLang === 'C++'}"
              @click.stop="switchForm()">sign in</button>
        </template>
        <template v-else>
          <p class="modal-win__title" :class="{'blue': this.$store.state.selectLang === 'C++'}">Sign in</p>
          <div class="modal-win__block">
            <input
                v-model.trim="userData.email"
                @focus="isInputFocusEmail = true;"
                @blur="isInputFocusEmail = false"
                @keyup="checkEmail"
                type="text"
                class="modal-win__block__input"
                :class="{'blue': this.$store.state.selectLang === 'C++'}">
            <span
                class="modal-win__block__placeholder"
                :class="{active: isInputFocusEmail || userData.email !== ''}">
            email
            </span>
          </div>
          <div class="modal-win__block">
            <input
                v-model.trim="userData.password"
                @focus="isInputFocusPass = true"
                @blur="isInputFocusPass = false"
                type="password"
                class="modal-win__block__input"
                :class="{'blue': this.$store.state.selectLang === 'C++'}">
            <span
                class="modal-win__block__placeholder"
                :class="{active: isInputFocusPass || userData.password !== ''}">
            password
            </span>
          </div>
          <button
              type="submit"
              class="modal-win__block__btn"
              @click.prevent="submitFormEnter">submit</button>
          <button
              type="button"
              class="modal-win__block__enter"
              :class="{'blue': this.$store.state.selectLang === 'C++'}"
              @click.stop="switchForm()">registration</button>
        </template>
      </form>
  </div>
</template>

<script>
import {mapState} from "vuex";

import api from '../services/api'
import axios from 'axios'
export default {
  name: 'the-modal-win',
  data() {
    return {
      showModal: true,
      ModalEnter: false,

      username: '',
      isCheckName: null,
      isInputFocusName: false,

      userEmail: '',
      isCheckEmail: null,
      isInputFocusEmail: false,

      userPassword: '',
      isCheckFieldPass: null,
      isInputFocusPass: false,
      isCheckPass: null,

      verifiedPassword: '',
      isInputFocusVerPass: false,
      isValidPassword: null,

      userData: {
        email: '',
        username: '',
        password: '',
      }
    }
  },
  methods: {
    async submitForm() {
      if( !this.isValidPassword || !this.isCheckPass || !this.isCheckName || !this.isCheckEmail) {
        this.$store.commit('updateErrorMassageCurrent', true)
      } else if(this.userData.username === '' || this.userData.email === '' || this.userData.password === '' || this.verifiedPassword === '') {
        this.$store.commit('updateErrorMassageVoid', true)
      }
      const response = await api.post('/api/v1/users/', this.userData)
        .then(response => {
          console.log(response)
          this.resetModalWin()
        })
        .catch(error => {
          alert(error)
        })
    },
    resetModalWin() {
      this.$store.commit('updateModalStatus', false);
      this.$store.commit('updateStatusAuthorization', true);
      this.$store.commit('closeErrorMassage', false)
      this.userData.username = '';
      this.userData.email = '';
      this.userData.password = '';
      this.verifiedPassword = '';
      this.isCheckFieldPass = null;
      this.isCheckName = null;
      this.isCheckPass = null;
      this.isValidPassword = null;
    },
    submitFormEnter() {
      if(this.username === '' || this.userPassword === '') {
        this.$store.commit('updateErrorMassageVoid', true)
      } else if(this.username !== this.$store.state.username  || this.userPassword !== this.$store.state.userPassword) {
        this.$store.commit('updateErrorMassageNon', true)
      } else {
        this.$store.commit('closeErrorMassage', false)
      }
    },
    switchForm() {
      this.ModalEnter = !this.ModalEnter;
      this.userData.username = '';
      this.isCheckName = null;
      this.userData.password = '';
      this.isCheckPass = null;
      this.verifiedPassword = '';
      this.isValidPassword = null;
    },
    closeModal(event) {
      if (!event.target.closest('.modal-win')) {
        this.$store.commit('updateModalStatus', false)
        document.getElementsByTagName('body')[0].classList.remove('lock')
      }
    },
    checkName() {
      this.userData.username !== '' && this.userData.username.length < 20 ? this.isCheckName = true : this.isCheckName = false
    },
    checkEmail() {
      let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      this.isCheckEmail = re.test(this.userData.email);
    },
    checkPass() {
      if(this.userData.password !== '') {
        return this.userData.password.length >= 8 ? this.isValidPassword = true : this.isValidPassword = false
      } else {
      }
    },
    checkVerifiedPass() {
      this.userData.password !== this.verifiedPassword ? this.isCheckPass = false : this.isCheckPass = true
    }
  },
}
</script>

<style src="@/style/modal-window.scss" lang="scss" scoped>

</style>
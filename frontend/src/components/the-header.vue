<template>
  <header class="header" :class="{active: this.$store.state.isActiveTask}">
    <div class="header-wrapper">
      <div class="header-wrapper__left">
        <div class="header-version">
          <button @click="openPageMain">
            <svg  xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path class="header-version__img" :class="{'blue': this.$store.state.selectLang === 'C++'}" d="M19 21C18.35 21 17.7667 20.8123 17.25 20.437C16.7333 20.0617 16.375 19.5827 16.175 19H11C9.9 19 8.95833 18.6083 8.175 17.825C7.39167 17.0417 7 16.1 7 15C7 13.9 7.39167 12.9583 8.175 12.175C8.95833 11.3917 9.9 11 11 11H13C13.55 11 14.021 10.804 14.413 10.412C14.805 10.02 15.0007 9.54933 15 9C15 8.45 14.804 7.979 14.412 7.587C14.02 7.195 13.5493 6.99933 13 7H7.825C7.60833 7.58333 7.24567 8.06267 6.737 8.438C6.22833 8.81333 5.64933 9.00067 5 9C4.16667 9 3.45833 8.70833 2.875 8.125C2.29167 7.54167 2 6.83333 2 6C2 5.16667 2.29167 4.45833 2.875 3.875C3.45833 3.29167 4.16667 3 5 3C5.65 3 6.22933 3.18767 6.738 3.563C7.24667 3.93833 7.60867 4.41733 7.824 5H13C14.1 5 15.0417 5.39167 15.825 6.175C16.6083 6.95833 17 7.9 17 9C17 10.1 16.6083 11.0417 15.825 11.825C15.0417 12.6083 14.1 13 13 13H11C10.45 13 9.979 13.196 9.587 13.588C9.195 13.98 8.99933 14.4507 9 15C9 15.55 9.196 16.021 9.588 16.413C9.98 16.805 10.4507 17.0007 11 17H16.175C16.3917 16.4167 16.7543 15.9373 17.263 15.562C17.7717 15.1867 18.3507 14.9993 19 15C19.8333 15 20.5417 15.2917 21.125 15.875C21.7083 16.4583 22 17.1667 22 18C22 18.8333 21.7083 19.5417 21.125 20.125C20.5417 20.7083 19.8333 21 19 21ZM5 7C5.28333 7 5.521 6.904 5.713 6.712C5.905 6.52 6.00067 6.28267 6 6C6 5.71667 5.904 5.479 5.712 5.287C5.52 5.095 5.28267 4.99933 5 5C4.71667 5 4.479 5.096 4.287 5.288C4.095 5.48 3.99933 5.71733 4 6C4 6.28333 4.096 6.521 4.288 6.713C4.48 6.905 4.71733 7.00067 5 7Z" fill="#FEB81C"/>
            </svg>
          </button>
          <span class="header-version__text desktop">Project version</span>
          <span class="header-version__text mobile">Proj. version</span>
          <div class="header-version__line"></div>
          <span class="header-version__text">1.0.0</span>
        </div>
      </div>
      <div class="header-wrapper__right">
        <button class="header-wrapper__alerts">
          <svg width="23" height="26" viewBox="0 0 23 26" xmlns="http://www.w3.org/2000/svg">
            <path d="M6.87609 22.1754V22.1754C8.63562 26.0236 14.1033 26.0231 15.8641 22.1754V22.1754M15.8641 22.1754H18.8579C22.2647 22.1754 23.7637 19.7193 18.8581 14.807C18.8581 5.47366 19.769 3.50875 11.3682 1.05261C3.29104 3.01752 3.87819 6.45612 3.87819 14.807C1.2936 17.2631 -1.11469 21.6842 3.8775 22.1754H15.8641Z" stroke="#313131" fill="#1e1d1b" stroke-width="3"/>
          </svg>
        </button>
        <router-link v-if="this.$store.state.isAuthorization" tag="button" to="/statistic" class="header-profile__link">
          <svg class="header-wrapper__profile" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
            <path d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z"/>
          </svg>
          <p class="header-profile__username">{{this.$store.state.username}}</p>
        </router-link>
        <button v-else type="button" class="header-profile__link" @click="openModalWin">
          <svg class="header-wrapper__profile" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
            <path d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z"/>
          </svg>
        </button>
<!--        <button class="header-wrapper__menu">-->
<!--          <span class="header-wrapper__menu__line"></span>-->
<!--          <span class="header-wrapper__menu__line"></span>-->
<!--          <span class="header-wrapper__menu__line"></span>-->
<!--        </button>-->
      </div>
    </div>
    <Transition name="fade">
      <the-modal-win v-if="this.$store.state.isModalVis">
      </the-modal-win>
    </Transition>
    <template v-if="this.$store.state.isErrorMassage">
      <the-massage @close-massage="CloseMassage">
        <template v-slot:massage-text>
          {{this.$store.state.isErrorMassageVoid}}
        </template>
      </the-massage>
    </template>
  </header>
</template>

<script>
import TheModalWin from "@/components/the-modal-window.vue";
import TheMassage from "@/components/the-message.vue";
import api from "@/services/api";

export default {
  name: 'the-header',
  components: {TheMassage, TheModalWin},
  data() {
    return {
    }
  },
  methods: {
    CloseMassage(val) {
      this.$store.commit('closeErrorMassage', val)
    },
    openModalWin() {
      this.$store.commit('updateModalStatus', true)
      document.getElementsByTagName('body')[0].classList.add('lock')
    },
    openPageMain() {
      this.$router.push('/')
    },
    async getUsername() {
      const response = await api.get('/api/v1/users/me')
          .then(response => {
            this.$store.state('setUserName', response.data.username)
            console.log(response.data.username)
          })
          .catch(error => {
            console.log(error)
          })
    },
  },
  mounted() {
    this.getUsername()
  }
}
</script>

<style src="@/style/header.scss" lang="scss" scoped>

</style>

<style>

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

</style>
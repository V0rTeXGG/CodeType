<template>
  <div class="statistics-wrapper">
    <div class="statistics-wrapper__top">
      <div class="statistics-account">
        <div class="statistics-account__wrapper-data">
          <svg class="statistics-account-img" xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 512 512">
            <path d="M399 384.2C376.9 345.8 335.4 320 288 320H224c-47.4 0-88.9 25.8-111 64.2c35.2 39.2 86.2 63.8 143 63.8s107.8-24.7 143-63.8zM0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256zm256 16a72 72 0 1 0 0-144 72 72 0 1 0 0 144z"/>
          </svg>
          <div class="statistics-account__left">
            <p class="statistics-account__username">{{username}}</p>
          </div>
        </div>
        <div class="statistics-account__level">
          <p class="statistics-account__level-num">1</p>
          <div class="statistics-account__level__bar">
            <div class="statistics-account__level__percent" :style="{width: 10 + '%'}"></div>
          </div>
        </div>
      </div>
      <div class="statistics-wrapper__line"></div>
      <div class="statistics-wrapper__data__block">
        <p class="statistics-wrapper__data__title">Tests completed</p>
        <p class="statistics-wrapper__data__value">0</p>
      </div>
      <div class="statistics-wrapper__data__block">
        <p class="statistics-wrapper__data__title">Time</p>
        <p class="statistics-wrapper__data__value">00:00:00</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'statistic-page',
  data() {
    return {
      username: '',
    }
  },
  mounted() {
    this.username = this.$store.state.username
  }
}
</script>

<style src="@/style/statistic.scss" lang="scss" scoped>

</style>
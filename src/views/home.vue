<template>
  <the-main-content/>
</template>

<script>


import TheMainContent from "@/components/the-main-content.vue";

export default {
  name: 'home-page',
  components: {TheMainContent},

  data() {
    return {

    }
  },
  mounted() {
    localStorage.setItem('isAuthorization', this.$store.state.isAuthorization)
  }
}
</script>

<style lang="scss" scoped>

</style>
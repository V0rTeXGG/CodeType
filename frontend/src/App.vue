<template>
  <the-sidebar/>
  <div class="main-content">
    <the-header/>
    <main class="main">
      <router-view/>
    </main>
  </div>
  <Transition name="fade">
    <the-loader v-if="isLoader"></the-loader>
  </Transition>
</template>

<script>
import TheHeader from "@/components/the-header.vue";
import TheSidebar from "@/components/the-sidebar.vue";
import TheLoader from "@/components/the-loader.vue";
import axios from "axios";

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit("initializeStore")

    const access = this.$store.state.access

    if (access) {
      axios.defaults.headers.common['Authorization'] = "JWT " + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  components: {TheHeader, TheSidebar, TheLoader},
  data() {
    return {
      isLoader: true
    }
  },
  methods: {
    loader() {
      setTimeout(() => this.isLoader = false, 300)
    }
  },
  mounted() {
    this.loader()
  }
}
</script>

<style src="@/style/main.scss" lang="scss">

</style>

<style>

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

</style>
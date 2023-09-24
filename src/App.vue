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
import TheLoader from "@/components/loader.vue";

export default {
  components:{TheHeader, TheSidebar, TheLoader},
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

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

</style>
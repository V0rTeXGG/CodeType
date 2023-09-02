<template>
  <the-sidebar/>
  <div class="main-content">
    <the-header/>
    <main class="main">
      <router-view/>
    </main>
  </div>
</template>

<script setup>
import TheHeader from "@/components/the-header.vue";
import TheSidebar from "@/components/the-sidebar.vue";
</script>

<style src="@/style/main.scss" lang="scss">

</style>
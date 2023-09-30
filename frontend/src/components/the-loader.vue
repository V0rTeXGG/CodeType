<template>
  <div class="loader">
    <div class="spinner" :class="{'blue': this.$store.state.selectLang === 'C++'}"></div>
  </div>
</template>

<script>
export default {
 name: 'the-loader',
  data() {
    return {

    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/style/varible";
.loader {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: $colorGrey;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.spinner {
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top: 4px solid $colorOrange;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

.spinner.blue {
  border-top: 4px solid $colorBlue;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

</style>
<template>
  <div class="massage-wrapper">
      <p class="massage-wrapper__text">
        <slot name="massage-text"></slot>
      </p>
      <button
          @click="closeMassage"
          class="massage-wrapper__close">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" class="massage-wrapper__img">
          <path d="M342.6 150.6c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L192 210.7 86.6 105.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L146.7 256 41.4 361.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L192 301.3 297.4 406.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3L237.3 256 342.6 150.6z"/>
        </svg>
      </button>
  </div>
</template>

<script>
export default {
  name: 'the-massage',
  data() {
    return {

    }
  },
  methods: {
    closeMassage() {
      this.$emit('closeMassage', false)
    }
  },
}
</script>

<style src="@/style/massage.scss" lang="scss" scoped>

</style>
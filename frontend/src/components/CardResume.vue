<template>
  <div class="card-area">
      <h3>BackEnd разработчик</h3>
      <h4>150 000 руб</h4>
      <RadioButton :item="resumeDetail" :tag='"resum"' v-model="select" />
  </div>
</template>

<script>
import RadioButton from '@/components/elements/RadioButton'
export default {
    name: 'CardResume',
    props: {
        resumeDetail: {
            type: Object,
        },
        select: {
            type: Number,
        }
    },
    components: {
        RadioButton
    },
    mounted() {
        console.error('Hi in card');
        console.log(this.resumeDetail);
    }
}
</script>

<style scoped>
    .card-area {
        width: 100px;
        background: purple;
    }
</style>
<template>
    <div class="gray-bg-color" v-if="show">
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: 'DialogWindow',
    props: {
        show: {
            type: Boolean
        }
    }
}
</script>

<style scoped>
.gray-bg-color {
    border: 2px solid purple;
    background: rgba(0, 0, 0, 0.192);
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
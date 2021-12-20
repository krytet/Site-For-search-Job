<template>
    <select v-model="modelValue" @change="changeOption">
        <option disabled value="">Сортировать по</option>
        <option 
            v-for="option in options"
            :value="option.value"
            :key="option.value"
        >
            {{ option.name }}
        </option>
    </select>
</template>

<script>
export default {
    name: 'SelectForList',
    props: {
        modelValue: {
            type: String,
        },
        options: {
            type: Array
        }
    },
    methods: {
        changeOption(event) {
            this.$emit('update:modelValue', event.target.value)
        }
    }
}
</script>

<style scoped>
select {
    border: none;
    color: #71717A;
    cursor: pointer;
    outline: none;
    appearance: none;
    text-align: end;
    width: 180px;
}

option {
    border: none;
    outline: none;
    width: 180px;
    appearance: none;
    padding: 10px;
    text-align: end;

}
</style>
<template>
    <label class="radio_select">
        <input type="radio" :name="tag" class="redio_select" v-model="modelValue" :value="item.id" @change="AddParamsToFilter">
        <span class="fake"></span>
        <span> {{ item.name }} </span>
    </label>
</template>

<script>
export default {
    name: 'RadioButton',
    props: {
        modelValue: {
            /**type: String*/
            type: Number
        },
        tag : {
            type: String
        },
        item: {
            type: Object,
        }
    },
    methods: {
        AddParamsToFilter(event) {

            console.log('event.target.value')
            console.log('value' ,event.target.value)
            console.log('key', event.target.name)
            /***this.$emit('update:modelValue', event.target.value)*/
            this.$emit('update:modelValue', event.target.value)
            
        }
    }
}
</script>

<style scoped>
    .radio_select {
        display: grid;
        grid-template-columns: 16px auto;
        grid-column-gap: 8px;
        text-align: left;
        color: #71717A;
        font-size: 14px;
        padding-bottom: 12px;
    }

    .radio_select input {
        display: none;
    }

    .fake {
        height: 14px;
        width: 14px;
        border: 1px solid #A1A1AA;
        border-radius: 50%;
        transition: 1s;
        position: relative;
    }

    .fake:hover {
        border: 1px solid #5c5c5c;
        transition: 0.2s;
    }

    .fake::before {
        content: "";
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: block;
        height: 3px;
        width: 3px;
        border-radius: 50%;
        border: 6px solid #7C3AED;
        transition: 0.5s;
        opacity: 0;
    }

    .redio_select:checked + .fake::before {
        opacity: 1;
    }
</style>
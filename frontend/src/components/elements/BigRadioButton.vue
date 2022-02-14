<template>
    <label class="radio_select">
        <input type="radio" :name="tag" class="redio_select" v-model="modelValue" :value="item.isComp" @change="SelectType">
        <span class="fake"></span>
        <!-- TODO Настроить заливание рамки  -->
        <span class="text-design"> {{ item.name }} </span>
    </label>
</template>

<script>
export default {
    name: 'BigRadioButton',
    props: {
        modelValue: {
            /**type: String*/
            type: Boolean
        },
        tag : {
            type: String
        },
        item: {
            type: Object,
        }
    },
    methods: {
        SelectType(event) {

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

    input.redio_select:checked + .fake::before {
        opacity: 1;
    }

    span.text-design {
        padding: 5px;
        border: 1px solid #A1A1AA;
        border-radius: 5px;
        color: black;
        display: block;
        
    }

    span.text-design:hover {
        background-color: #7c3aed50;
        transition: 0.4s;
    }

    input.redio_select:checked + span.text-design {
        color: rgb(255, 0, 0);
        background-color: #7C3AED;
    }

</style>
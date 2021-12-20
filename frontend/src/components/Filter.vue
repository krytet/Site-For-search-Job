<template>
    <div id="left_sidebar" class="left_sidebar">
        <h5>Фильтр</h5>
        <h2 > {{ modelValue.experience }} </h2> <!-- TODO сделать динамичным -->
        <div v-for="radio in filters_elements.radio" :key="radio.value">
            <h5> {{ radio.name }} </h5>
            <RadioButton 
                v-for="item in radio.items"
                v-model:modelValue="modelValue[radio.value]"
                :item='item' 
                :tag='radio.value' 
                :key="item.id"
                @change="ChangeRadio"
            />
        </div>
        
        <div v-for="switch_elements in filters_elements.switch_elements" :key="switch_elements.value">
            <Switch 
                :element='switch_elements'
                @change="ChangeSwitch" 
            />
        </div>
    </div>
</template>

<script>
import RadioButton from '@/components/elements/RadioButton'
import Switch from '@/components/elements/Switch'

export default {
    name: 'Filter',
    data() {
        return {
            /**filtersParams: '',**/
            filtersParams: Object,
        }
    },
    props: {
        modelValue: {
            type: Object
        },
        filters_elements: {
            type: Object
        }
    },
    components: {
        RadioButton, Switch
    },
    methods: {
        ChangeRadio(event) {

            //this.filtersParams[event.target.name] = event.target.value
            //this.modelChecked[event.target.name] = event.target.value

            this.$emit('update:modelChecked', this.modelValue)
            
        },
        ChangeSwitch(event) {

            if  (!this.modelValue[event.target.name]){
                console.log('true');
                this.modelValue[event.target.name] = true;
            }else {
                console.log('False');
                this.modelValue[event.target.name] = ''
            }


            
        },
    }
}
</script>

<style scoped>
    .left_sidebar h5 {
        color: #18181B;
        font-size: 16px;
        margin-bottom: 12px;
    }

    .left_sidebar div h5 {
        margin-top: 0px;
    }

</style>
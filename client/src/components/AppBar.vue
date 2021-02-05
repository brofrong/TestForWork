<template>
  <v-app-bar
      app
      color="primary"
      dark
    >
    <v-btn
        @click="changeEditView"
    >
        <div v-if="isEdit">
            Добавить
            <v-icon>
                mdi-plus
            </v-icon>
        </div>
        <div v-else>
            Смотреть
            <v-icon>
                mdi-card-search
            </v-icon>
        </div>
    </v-btn>
    </v-app-bar>
</template>

<script>
export default {
    data:() =>{
        return{
            isEdit:true
        }
    },
    methods:{
        changeEditView() {
         this.isEdit = !this.isEdit
         this.$emit('change')   
        }
    }
}
</script>
    
<style>

</style>
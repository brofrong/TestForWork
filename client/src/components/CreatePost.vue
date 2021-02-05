<template>
    <v-container> 
        <v-row 
            no-gutters 
            justify ='space-between'
        >
            <v-col md="5" sm="12"> 
                <v-form
                    class="ma-5"
                >
                        <v-text-field
                            v-model="name"
                            label="Название языка программирования"
                            placeholder="JavaScript"
                            required
                        >
                        </v-text-field>
                        <v-text-field
                            v-model="imgsrc"
                            label="Ссылка на картинку"
                            placeholder="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/80px-Unofficial_JavaScript_logo_2.svg.png"
                            required
                        >
                        </v-text-field>
                        <v-textarea
                            v-model="aboutlanguage"
                            label="О языке программирования"
                            placeholder="Класный язык"
                            required
                        >
                        </v-textarea>
                        <v-text-field
                            v-model="tags"
                            label="Теги через запятую"
                            placeholder="WEB,JS,ошибка в 2034 строке"
                            required
                        >
                        </v-text-field>
                        <v-btn
                            class="mr-4"
                            @click="submit"
                            :loading="loading"
                            >
                            отправить
                        </v-btn>   
                </v-form>
                <v-dialog
                    v-model="dialog"
                    hide-overlay
                    persistent
                    width="300"
                    >
                    <v-card>

                        <v-card-text>
                            Язык программирования успешно добавлен
                        </v-card-text>

                        <v-divider></v-divider>

                        <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="primary"
                            text
                            @click="dialog = false"
                        >
                            ок
                        </v-btn>
                        </v-card-actions>
                    </v-card>
                    </v-dialog>
            </v-col >
            <v-col md="5" sm="12">
                <h2>Предпросмотр:</h2>
                <Card
                    :name="name"
                    :imgsrc="imgsrc"
                    :aboutlanguage="aboutlanguage"
                    :tags="cardTags"
                />
            </v-col>
        </v-row>
    </v-container>
</template>

<script>

import Card from './Card'

export default {
    components:{
        Card
    },

    data: () =>{
        return{
            name: '',
            imgsrc: '',
            aboutlanguage:'',
            tags:'',

            loading:false,
            dialog:false
        }
    },
    computed:{
        cardTags(){
            return this.tags.split(',')
        }
    },
    methods:{
        submit (){
            this.loading = true;
            var toServer={
                name:this.name,
                imgsrc:this.imgsrc,
                about:this.aboutlanguage,
                tags:this.tags
            }
            this.$axios
                .post(this.$hostname+"/newpost",toServer)
                .then(response => {
                    this.loading = false
                    if(response.data=="ok"){
                        this.name = ''
                        this.imgsrc = ''
                        this.aboutlanguage = ''
                        this.tags = ''
                        
                        this.dialog = true
                    }
                })
                .catch(error => console.log(error))
        }
    }
}
</script>

<style>

</style>
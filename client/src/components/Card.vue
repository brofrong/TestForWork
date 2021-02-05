<template>
  <v-card
                        elevation="2"
                        class="ma-6 pa-2"
                        width="380"
                        height="560">
                    <v-img
                        aspect-ratio=1
                        contain
                        :src="imgsrc"
                        class="align-end"
                        height="250"
                        width="370"
                    >
                    
                    <v-card-title
                        
                    >
                            {{ name }}
                    </v-card-title>
                    </v-img>
                    <v-card-text>
                        <v-chip-group
                            column
                            
                        >
                            <v-chip v-for="tag in tags" :key="tag"
                                small
                            >
                                {{tag}}
                            </v-chip>
                        </v-chip-group>
                    </v-card-text>
                    <v-card-text
                        class="scrolable"
                    >
                        <p class="text--primary text-start">
                            <b>О себе:</b>
                            {{ aboutlanguage }}
                        </p>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                            <v-chip class='mr-2'>
                                {{dislikes}}
                                <v-icon color=red>mdi-close</v-icon>
                            </v-chip>
                            <v-chip>
                                {{likes}}
                            <v-icon class='mr-2' color=green>mdi-heart</v-icon>                           
                            </v-chip>
                    </v-card-actions>
                </v-card>
</template>

<script>
export default {
    props: ['name', 'imgsrc', 'aboutlanguage', 'tags','likes','dislikes'],
}
</script>

<style>
.scrolable{
    overflow: auto;
    height: 150px;
}   

</style>
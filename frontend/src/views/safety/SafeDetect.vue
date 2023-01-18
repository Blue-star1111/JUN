<template>
  <v-main>
    <br>
    <div class="text-center" style="margin-top: -5%">
        <h1>This is an SAFETY page</h1>
    </div>
    <v-container fluid>
      <hr>
      <hr><br>
      <v-flex>
        <v-col></v-col>
        <v-col class="detect" style="width:60%">
          <v-card style="height:640px; width:640px; margin-left:2.5%;">
            <!-- <img :src="image" alt=""> -->
          </v-card>
        </v-col>
        <v-col></v-col>
      </v-flex>

      <div class="text-center">
        <form method="post" enctype="multipart/form-data">
          <div>
            <!-- <input ref="image" @change="uploadImg()" type="file" id="chooseFile" name="chooseFile" accept="image/*"> -->
          </div>
        </form>
        <br>
        <v-btn
          class="send-button"
          to="/safety/"
          rounded
          color="blue"
          dark
        >
          다른 사진 판별하기
        </v-btn>
      </div>  
      <br><br>
    </v-container>
  </v-main>
</template>
  
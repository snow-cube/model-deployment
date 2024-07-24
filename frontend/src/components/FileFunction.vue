<script setup>
import axios from "axios"
import { ref, onMounted, computed } from 'vue'

// 响应式状态
const file = ref(null)
const uploadFileName = ref("未选择文件")
const downloadFileName = ref("")
const resultImgName = ref("")

const resultImgPath = computed(() => {
    return "http://localhost:8000/download?filename=" + resultImgName.value
})

// 选取文件
function getFile(event) {
    file.value = event.target.files[0];
    // alert(file.value.name);
    uploadFileName.value = file.value.name;
}


// 上传文件 (POST)
function upload() {
    let url = "http://localhost:8000/upload";
    let formData = new FormData();
    formData.append("name", "zhangsan");
    formData.append("age", "18");
    formData.append("token", "test_token");
    formData.append("file", file.value);
    let config = {
        headers: {
            "Content-Type": "multipart/form-data/"
        }
    }
    axios.post(url, formData, config).then((res) => {
        downloadFileName.value = res.data.filename;
        resultImgName.value = res.data.imgname;
        // console.log(res)
        alert("上传成功!");
    }).catch(() => {
        alert("请先上传文件!");
    })
}


// 下载带链接文件 (window.open)
function downloadLink() {
    if (downloadFileName.value) {
        window.open("http://localhost:8000/download?filename=" + downloadFileName.value);
    }
}
</script>


<template>
    <div class="module-box">
        <h3 class="box-title">模型输入</h3>
        <div class="box-content">
            <div id="file-select">
                <input id="file-input" type="file" @change="getFile($event)" />
                <label type="button" for="file-input" class="select-btn">
                    选择文件
                </label>
                <span class="file-name">{{ uploadFileName }}</span>
            </div>
            <el-button :class="{ disabled: file === null }" class="file-btn" type="primary" @click="upload">上传文件</el-button>
        </div>
    </div>
    <div class="module-box">
        <h3 class="box-title">模型输出</h3>
        <div class="box-content">
            <el-button :class="{ disabled: !downloadFileName }" class="file-btn" type="primary" @click="downloadLink">下载</el-button>
            <img v-if="resultImgName" :src="resultImgPath" alt="Result image" id="result-show" />
        </div>
    </div>
</template>


<style scoped>
    .module-box {
        /* padding: 20px; */
        /* background-color: aqua; */
        margin: 20px 0;
    }

    .box-title {
        background-color: #923339;
        font-family: Arial, Helvetica, sans-serif;
        font-weight: bold;
        color: white;
        padding: 5px 30px;
        border-style: solid;
        border-color: #923339;
        border-width: 1px 1px 0 1px;
        border-radius: 7px 7px 0 0;
    }

    .box-content {
        padding: 10px 30px;
        /* background-color: grey; */
        border-style: solid;
        border-color: #923339;
        border-width: 0 1px 1px 1px;
        border-radius: 0 0 7px 7px;
    }

    #file-select {
        height: 50px;
        margin: 5px 0;
    }

    .select-btn {
        background-color: #DC636C;
        /* padding: 0 10px; */
        text-align: center;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 1.1em;
        /* font-weight: bold; */
        color: white;
        display: block;
        width: 150px;
        height: 40px;
        line-height: 38px; /* 需为 height 减去上下边框 */
        float: left;
        border-style: solid;
        border-color: #DC636C;
        border-width: 1px 1px 1px 1px;
        border-radius: 7px 0 0 7px;
    }

    .select-btn:hover {
        background-color: #e4747b;
    }

    .file-name {
        display: block;
        min-width: 600px;
        font-size: 1.1em;
        font-family: Consolas, monospace;
        padding: 0 15px;
        height: 40px;
        line-height: 38px; /* 需为 height 减去上下边框 */
        float: left;
        border-style: solid;
        border-width: 1px 1px 1px 0;
        border-color: #DC636C;
        border-radius: 0 7px 7px 0;
    }

    .file-btn {
        display: block;
        /* margin: 20px; */
        background-color: #DC636C;
        padding: 7px 0;
        text-align: center;
        width: 150px;

        font-family: Arial, Helvetica, sans-serif;
        font-size: 1.1em;
        /* font-weight: bold; */
        color: white;
        border-radius: 7px;
        margin: 5px 0;
    }

    .file-btn:hover {
        background-color: #e4747b;
    }

    .file-btn.disabled {
        background-color: #fcd2d2;
    }

    #file-input {
        display: none;
    }

    #result-show {
        max-width: 1000px;
        display: block;
        margin: 10px;
    }
</style>
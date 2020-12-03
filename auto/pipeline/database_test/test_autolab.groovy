// 定义测试场景文件路径变量
def testplan = "./auto/plan/database_test/test_autolab.py"

// 声明式  pipeline 替代node
node {
    // init Python运行环境
    // 初始化一些运行态需要的全局变量
    stage("Init"){
        echo "Init Run Env"
    }

    // 从git获取最新代码
    stage("Check out"){
        echo "check out last code"
        checkout scm
    }

    // 启动测试
    stage("Test"){
        powershell "pytest --version"
        dir("."){
            powershell "pwd"
            powershell "pytest ${testplan} --html=./logs/report.html --self-contained-html"
        }
    }

    // 发布html报告
    stage("Report"){
        dir("."){
            publishHTML (target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'logs',
                reportFiles: 'report.html',
                reportName: "HTML Report"
            ])
        }
    }

    // 发布通知消息
    stage("Notify"){
        script{
            if( currentBuild.currentResult == "SUCCESS"){
                // build success， do nothing
                echo "It's build SUCCESS"
                //dingTalk accessToken: "https://oapi.dingtalk.com/robot/send?access_token=${DING_TOKEN}", imageUrl: '', jenkinsUrl: 'http://127.0.0.1:8080/jenkins/', message: "项目: ${currentBuild.projectName} \n构建号:#${currentBuild.number} \n结果: ${currentBuild.currentResult}" , notifyPeople: ''
            }
            else{
                // build failure or abort send dingTalk
                echo "It's buuild Failed"
                //dingTalk accessToken: "https://oapi.dingtalk.com/robot/send?access_token=${DING_TOKEN}", imageUrl: '', jenkinsUrl: 'http://127.0.0.1:8080/jenkins/', message: "项目: ${currentBuild.projectName} \n构建号:#${currentBuild.number} \n结果: ${currentBuild.currentResult}" , notifyPeople: ''
            }
        }
    }
}
/*
node {
    // 初始化Python运行环境
    stage("Init Env"){
        // env.PATH = "${env.VIRTUAL_ENV}:${env.PATH}"
    }

    // 从git拉取代码stage
    stage('check out') {
        checkout scm
    }

    // 启动测试stage
    stage('Test')
        // for linux/unix/mac
        // sh "pytest --version"

        dir("./AutoLab"){
            powershell "pwd"
            powershell "pytest ${testfile} --html=./logs/report.html --self-contained-html"
        }
    }

    // 发布html报告
    stage('Report') {
        dir("./AutoLab"){
            publishHTML (target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'logs',
                reportFiles: 'report.html',
                reportName: "HTML Report"
            ])
        }
    }

    // 如果没成功，则往测试群发送钉钉通知
    stage('Notify'){
        script{
            if( currentBuild.currentResult == "SUCCESS"){
                // build success， do nothing
                echo "it's build SUCCESS"
                //dingTalk accessToken: "https://oapi.dingtalk.com/robot/send?access_token=${DING_TOKEN}", imageUrl: '', jenkinsUrl: 'http://127.0.0.1:8080/jenkins/', message: "项目: ${currentBuild.projectName} \n构建号:#${currentBuild.number} \n结果: ${currentBuild.currentResult}" , notifyPeople: ''
            }
            else{
                // build failure or abort send dingTalk
                // dingTalk accessToken: "https://oapi.dingtalk.com/robot/send?access_token=${DING_TOKEN}", imageUrl: '', jenkinsUrl: 'http://127.0.0.1:8080/jenkins/', message: "项目: ${currentBuild.projectName} \n构建号:#${currentBuild.number} \n结果: ${currentBuild.currentResult}" , notifyPeople: ''
                echo "it's build failed"
            }
        }
    }

}

def testplan = "./auto/plan/database_test/test_autolab.py"

node {
    stage("Init"){
        echo "Init Run Env"
    }

    stage("Check out"){
        echo "check out last code"
        checkout scm

    }

    stage("Test"){
        powershell "pytest --version"
        dir("."){
            powershell "pwd"
            powershell "pytest ${testplan} --html=./logs/report.html --self-contained-html"
        }
    }

    stage("Report"){
        dir("."){
            publishHTML (target:[
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'logs',
                reportFiles: 'report.html',
                reportName: "HTML Report"
            ])
        }
    }

    stage("Notify"){
        script{
            if ( currentBuild.currentResult == "SUCCESS"){
                echo "it is build success"
            }
            else{
                echo "it is build failed"
            }
        }
    }
}

*/
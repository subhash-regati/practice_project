pipeline{
    agent any
    stages{
        stage('fist_stage'){
            steps{
            echo 'first build started'
            build job: 'second_job', parameters: [string(name: 'string1', value: 'sam')]
            }
        }
        stage('second_stage'){
            steps{
            echo 'second build'
            build job: 'forth_job'
            }
        }
        stage('third_stage'){
            steps{
            echo 'third build is ready'
            build job: 'third_job'
            }
        }
            
    }
    post{
        always{
            echo 'build completed'
            }
    }
}

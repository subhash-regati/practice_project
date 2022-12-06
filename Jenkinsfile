pipeline{
    agent any
    environment{
        SERVER_CREDENTIALS=credentials('server_cred')
        NEW_VERSION='1.0.0.1'
    }
    parameters{
        choice(name:'string_input',choices:['sam','ram','hari','subhash'],description:'')
        booleanParam(name:'execute_stage',defaultValue:true,description:'')                                            
    }
    stages{
        stage('fist_stage'){
            steps{
            echo "Build version :${NEW_vERSION}"
            echo 'first build started'
            build job: 'second_job', parameters: [string(name: 'string1', value: 'sam')]
            }
        }
        stage('second_stage'){
            when{
                    expession{
                        BRANCH_NAME =='master'
                    }
                }
            steps{
                echo 'second build'
                build job: 'forth_job'
            }
        }
        stage('third_stage'){
            steps{
                when{
                    expression{
                        param.execute_stage == 'true'
                    }
                }
            echo 'third build is ready'
            build job: 'third_job'
            }
        }
            
    }
    post{
        always{
            echo 'build completed'
            echo "sever credentials ${SERVER_CREDENTIALS}"
            echo "string name is ${param.string_input}"
            }
    }
}

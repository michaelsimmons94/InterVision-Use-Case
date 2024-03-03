import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Function, Runtime, Code} from 'aws-cdk-lib/aws-lambda'
import { resolve } from 'path';
import { Effect, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { CfnIntegrationAssociation } from 'aws-cdk-lib/aws-connect';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class AstrologerOnDemandStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const connectInstanceId = "arn:aws:connect:us-east-1:634176862156:instance/4a1a2f31-cd10-45b0-ad39-1a6c6e16fff9"
    const lookupSign = new Function(this, 'lookupSign', {
      runtime: Runtime.PYTHON_3_12,
      handler: 'lookup_sign.handler.handler',
      code: Code.fromAsset(resolve(__dirname, '../src/')),
      functionName: 'lookupSign'
    });
    new CfnIntegrationAssociation(this, 'lookupSignIntegration', {
      instanceId: connectInstanceId,
      integrationType: 'LAMBDA_FUNCTION',
      integrationArn: lookupSign.functionArn,
    });
    const generateHoroscope = new Function(this, 'generateHoroscope', {
      runtime: Runtime.PYTHON_3_12,
      handler: 'generate_horoscope.handler.handler',
      code: Code.fromAsset(resolve(__dirname, '../src/')),
      functionName: 'generateHoroscope',
      timeout: cdk.Duration.seconds(30)
    });
    new CfnIntegrationAssociation(this, 'generateHoroscopeIntegration', {
      instanceId: connectInstanceId,
      integrationType: 'LAMBDA_FUNCTION',
      integrationArn: generateHoroscope.functionArn,
    });
    generateHoroscope.addToRolePolicy(new PolicyStatement({
      actions: ["bedrock:InvokeModel"],
      resources: ["*"],
      effect: Effect.ALLOW
    }))
  }
}

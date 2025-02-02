import {
  GetParameterCommand,
  SSMClient,
} from "npm:@aws-sdk/client-ssm@^3.315.0";

const REGION = 'us-east-1'

export const getParameterByNameBuilder = async (region: string): Promise<(name: string) => Promise<string>> => {
  return async (name: string) => {
    const ssmClient = new SSMClient({ region: REGION });
    try {
      const { Parameter } = await ssmClient.send(
        new GetParameterCommand({
          Name: name,
          WithDecryption: true,
        }),
      );

      if (Parameter?.Value == null) {
        throw new Error(
          `No parameters found for ${name}.`,
        );
      }

      return Parameter.Value;
    } finally {
      ssmClient.destroy();
    }

  }
};

export const getParameterByName = getParameterByNameBuilder(REGION)

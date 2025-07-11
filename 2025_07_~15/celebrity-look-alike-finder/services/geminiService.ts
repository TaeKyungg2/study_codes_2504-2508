
import { GoogleGenAI, Type } from "@google/genai";
import { CelebrityResult } from '../types';

if (!process.env.API_KEY) {
    throw new Error("API_KEY environment variable not set");
}

const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });

const celebritySchema = {
  type: Type.OBJECT,
  properties: {
    celebrityName: {
      type: Type.STRING,
      description: "가장 닮았다고 생각하는 한국 연예인의 이름.",
    },
    similarity: {
      type: Type.INTEGER,
      description: "사진의 인물과 해당 연예인이 얼마나 닮았는지 1부터 100 사이의 퍼센트(%) 값.",
    },
    reason: {
      type: Type.STRING,
      description: "왜 그렇게 생각하는지에 대한 1~2문장의 간략한 이유. (예: 눈매, 얼굴형 등)",
    },
  },
  required: ["celebrityName", "similarity", "reason"],
};

export const findCelebrityLookAlike = async (base64Image: string, mimeType: string): Promise<CelebrityResult> => {
    try {
        const imagePart = {
            inlineData: {
                mimeType: mimeType,
                data: base64Image,
            },
        };

        const textPart = {
            text: "이 사진 속 인물과 가장 닮은 한국 연예인을 한 명 찾아주세요. 이름, 닮은 정도를 퍼센트로, 그리고 왜 그렇게 생각하는지에 대한 간단한 이유를 JSON 형식으로 알려주세요. 영어 이름 대신 한국어 이름으로 알려주세요. 만약 사진에 얼굴이 없다면, celebrityName을 'N/A'로 설정해주세요.",
        };

        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: { parts: [textPart, imagePart] },
            config: {
                responseMimeType: "application/json",
                responseSchema: celebritySchema,
            }
        });

        const jsonText = response.text.trim();
        const result = JSON.parse(jsonText) as CelebrityResult;

        if (result.celebrityName === 'N/A') {
          throw new Error("사진에서 얼굴을 찾을 수 없습니다. 얼굴이 잘 보이는 사진으로 다시 시도해주세요.");
        }

        return result;
    } catch (error) {
        console.error("Gemini API call failed:", error);
        if (error instanceof Error && error.message.includes("얼굴을 찾을 수 없습니다")) {
            throw error;
        }
        throw new Error("AI 분석에 실패했습니다. 이미지나 프롬프트를 확인해주세요.");
    }
};

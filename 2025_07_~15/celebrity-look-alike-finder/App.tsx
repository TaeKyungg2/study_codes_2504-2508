
import React, { useState, useCallback } from 'react';
import { CelebrityResult } from './types';
import { findCelebrityLookAlike } from './services/geminiService';
import { UploadIcon, PhotoIcon, SparklesIcon, ArrowPathIcon } from './components/IconComponents';
import { Spinner } from './components/Spinner';

// Helper function defined outside the component to prevent recreation on re-renders
const fileToBase64 = (file: File): Promise<string> => {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
      // Result is "data:image/jpeg;base64,LzlqLzRBQ...". We need to remove the prefix.
      const base64String = (reader.result as string).split(',')[1];
      resolve(base64String);
    };
    reader.onerror = error => reject(error);
  });
};

const ImageUploader: React.FC<{ onImageUpload: (file: File) => void }> = ({ onImageUpload }) => {
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      onImageUpload(file);
    }
  };

  const handleDragOver = (event: React.DragEvent<HTMLLabelElement>) => {
    event.preventDefault();
  };

  const handleDrop = (event: React.DragEvent<HTMLLabelElement>) => {
    event.preventDefault();
    const file = event.dataTransfer.files?.[0];
    if (file) {
      onImageUpload(file);
    }
  };

  return (
    <div className="w-full max-w-lg mx-auto">
      <label
        htmlFor="file-upload"
        className="relative block w-full h-64 border-2 border-dashed border-slate-500 rounded-xl text-center cursor-pointer hover:border-cyan-400 transition-colors duration-300"
        onDragOver={handleDragOver}
        onDrop={handleDrop}
      >
        <div className="flex flex-col justify-center items-center h-full">
          <UploadIcon className="w-16 h-16 text-slate-500 mb-4" />
          <span className="text-xl font-semibold text-slate-300">사진을 드래그하거나 클릭하여 업로드</span>
          <p className="mt-2 text-sm text-slate-400">가장 잘 나온 얼굴 사진을 올려주세요</p>
        </div>
        <input id="file-upload" name="file-upload" type="file" className="sr-only" accept="image/*" onChange={handleFileChange} />
      </label>
    </div>
  );
};


const ResultDisplay: React.FC<{ userImage: string; result: CelebrityResult; onReset: () => void; }> = ({ userImage, result, onReset }) => {
  const celebrityImageUrl = `https://picsum.photos/seed/${result.celebrityName.replace(/\s/g, '')}/512/512`;

  return (
    <div className="w-full max-w-4xl mx-auto animate-fade-in">
        <div className="bg-slate-800/50 backdrop-blur-sm p-8 rounded-2xl shadow-2xl ring-1 ring-slate-700">
            <h2 className="text-center text-3xl font-bold mb-2 text-cyan-300 flex items-center justify-center">
                <SparklesIcon className="w-8 h-8 mr-2" /> 분석 결과
            </h2>
            <p className="text-center text-slate-300 mb-8">당신은 <span className="font-bold text-white text-lg">{result.celebrityName}</span>님을 <span className="font-bold text-white text-lg">{result.similarity}%</span> 닮았어요!</p>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                {/* User Image */}
                <div className="text-center">
                    <h3 className="font-bold text-xl mb-4 text-slate-200">당신의 사진</h3>
                    <img src={userImage} alt="User" className="rounded-xl shadow-lg w-full h-auto aspect-square object-cover" />
                </div>
                {/* Celebrity Image */}
                <div className="text-center">
                    <h3 className="font-bold text-xl mb-4 text-slate-200">{result.celebrityName}</h3>
                    <img src={celebrityImageUrl} alt={result.celebrityName} className="rounded-xl shadow-lg w-full h-auto aspect-square object-cover" />
                </div>
            </div>

            <div className="mt-8 bg-slate-700/50 p-6 rounded-xl">
                <h4 className="font-semibold text-lg text-slate-100 mb-2">AI 분석 코멘트:</h4>
                <p className="text-slate-300 leading-relaxed">{result.reason}</p>
            </div>
        </div>

        <div className="text-center mt-8">
            <button
                onClick={onReset}
                className="bg-cyan-500 text-white font-bold py-3 px-8 rounded-full hover:bg-cyan-400 transition-all duration-300 shadow-lg hover:shadow-cyan-500/50 flex items-center mx-auto"
            >
                <ArrowPathIcon className="w-5 h-5 mr-2" />
                다시 해보기
            </button>
        </div>
    </div>
  );
};


export default function App() {
  const [imageFile, setImageFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [result, setResult] = useState<CelebrityResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleImageUpload = (file: File) => {
    setImageFile(file);
    setPreviewUrl(URL.createObjectURL(file));
    setResult(null);
    setError(null);
  };

  const handleAnalyzeClick = useCallback(async () => {
    if (!imageFile) return;

    setIsLoading(true);
    setError(null);

    try {
      const base64Image = await fileToBase64(imageFile);
      const analysisResult = await findCelebrityLookAlike(base64Image, imageFile.type);
      setResult(analysisResult);
    } catch (err) {
      console.error(err);
      setError('분석 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.');
    } finally {
      setIsLoading(false);
    }
  }, [imageFile]);

  const handleReset = () => {
    setImageFile(null);
    setPreviewUrl(null);
    setResult(null);
    setError(null);
    setIsLoading(false);
  };

  return (
    <div className="min-h-screen w-full flex flex-col items-center justify-center p-4 sm:p-6 lg:p-8 bg-slate-900 bg-grid-slate-700/[0.2]">
      <div className="w-full max-w-4xl mx-auto text-center mb-12">
        <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight text-white">
          AI 연예인 닮은꼴 찾기
        </h1>
        <p className="mt-4 text-lg text-slate-300 max-w-2xl mx-auto">
          얼굴 사진을 업로드하여 어떤 연예인과 닮았는지 확인해보세요!
        </p>
      </div>
      
      <main className="w-full">
        {error && (
            <div className="bg-red-500/20 border border-red-500 text-red-300 p-4 rounded-lg text-center mb-6 max-w-lg mx-auto">
                <p>{error}</p>
            </div>
        )}

        {!result && !previewUrl && <ImageUploader onImageUpload={handleImageUpload} />}

        {previewUrl && !result && (
          <div className="w-full max-w-lg mx-auto text-center animate-fade-in">
              <div className="relative">
                  <img src={previewUrl} alt="Preview" className="rounded-xl shadow-2xl w-full h-auto aspect-square object-cover" />
                  {isLoading && (
                      <div className="absolute inset-0 bg-slate-900/70 flex flex-col items-center justify-center rounded-xl">
                          <Spinner />
                          <p className="text-lg mt-4 font-semibold">얼굴을 분석하고 있습니다...</p>
                      </div>
                  )}
              </div>
              <button
                  onClick={handleAnalyzeClick}
                  disabled={isLoading}
                  className="mt-8 bg-cyan-500 text-white font-bold py-3 px-8 rounded-full hover:bg-cyan-400 transition-all duration-300 disabled:bg-slate-600 disabled:cursor-not-allowed shadow-lg hover:shadow-cyan-500/50 flex items-center mx-auto"
              >
                  <PhotoIcon className="w-6 h-6 mr-3" />
                  {isLoading ? '분석 중...' : '닮은 연예인 찾기'}
              </button>
          </div>
        )}

        {result && previewUrl && (
          <ResultDisplay userImage={previewUrl} result={result} onReset={handleReset} />
        )}
      </main>
      
      <footer className="text-center text-slate-500 mt-12 text-sm">
        <p>Powered by Google Gemini. 이미지는 결과 확인 후 즉시 삭제됩니다.</p>
      </footer>
    </div>
  );
}

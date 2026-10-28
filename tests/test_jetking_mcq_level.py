"""QA for lesson MCQs calibrated to the 16-question teacher reference.

These are pedagogical examples, NOT assertions about an official exam bank.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons" / "chapters"

# Correct answer CONTENT, not letter: option order is deliberately shuffled.
EXPECTED = {
    "PY-24": ["11", "10", "(−4, 2)", "0"],
    "PY-25": ["10", "1", "It has no inverse | Nó không có ma trận nghịch đảo", "(2, 4)"],
    "PY-26": ["x = 5, y = 2", "No solution | Vô nghiệm", "0",
              "Yes, both equations hold | Có, cả hai đều đúng"],
    "PY-27": ["3", "90%", "The x-axis | Trục x", "20%"],
    "PY-28": ["11", "3",
              "Exponential growth multiplies by a fixed factor in equal steps | Tăng trưởng mũ nhân theo một tỷ lệ cố định qua các bước đều",
              "0"],
    "PY-29": ["0", "0.5", "1",
              "The output lies strictly between 0 and 1 | Kết quả nằm giữa 0 và 1, không chạm hai đầu"],
    "PY-30": ["2.5", "1.5", "0.9", "Mean squared error | MSE"],
    "PY-31": ["8x − 3", "4", "0", "It is continuous at x = a | Hàm liên tục tại x = a"],
    "PY-32": ["6", "3.5", "Loss may oscillate or diverge | Loss có thể dao động hoặc phân kỳ",
              "It is a stationary point, not necessarily a minimum | Đây là điểm dừng, chưa chắc là cực tiểu"],
    "PY-33": ["[[2, 0], [0, 2]]", "x = 3",
              "A strict local minimum | Một cực tiểu địa phương nghiêm ngặt",
              "Saddle point | Điểm yên ngựa"],
    "PY-34": ["0.5", "0.65", "1/3", "0.25"],
    "PY-35": ["0.18", "0.4",
              "P(A|B) always equals P(B|A) | P(A|B) luôn bằng P(B|A)", "0.5"],
    "PY-36": ["0.5", "0.5", "It spreads out more | Phân phối trải rộng hơn",
              "They are equal | Hai giá trị bằng nhau"],
    "PY-37": ["3", "2", "5", "When all observations are equal | Khi tất cả quan sát bằng nhau"],
    "PY-38": ["6", "19",
              "It needs checking, but is not necessarily wrong | Nên kiểm tra, nhưng chưa chắc là dữ liệu sai",
              "Mean > median often | Trung bình thường lớn hơn trung vị"],
    "PY-39": ["5", "It halves | Giảm một nửa",
              "No; it only helps reproduce the random draw | Không; seed chỉ giúp tái lập lượt lấy mẫu",
              "The distribution of sample means tends toward normal | Phân phối trung bình mẫu tiến gần phân phối chuẩn"],
    "PY-40": ["Reject H0 | Bác bỏ H0",
              "Fail to reject H0 | Chưa đủ bằng chứng để bác bỏ H0",
              "Fail to reject H0 | Chưa bác bỏ H0",
              "Probability of observing results this extreme or more if H0 were true | Xác suất gặp kết quả cực đoan bằng hoặc hơn nếu H0 đúng"],
}

class TeacherLevelMCQTests(unittest.TestCase):
    def test_calibrated_questions_have_verified_correct_answer_content(self):
        self.assertEqual(len(EXPECTED), 17)
        reviewed = 0
        for lesson_id, answers in EXPECTED.items():
            with self.subTest(lesson=lesson_id):
                paths = list(LESSONS.glob(lesson_id + "-*.vi.md"))
                self.assertEqual(len(paths), 1)
                source = paths[0].read_text(encoding="utf-8")
                quiz = source.split("## 7. Trắc nghiệm", 1)[1].split("## 8.", 1)[0]
                chunks = re.split(r"(?=^\*\*Q\d+\.)", quiz, flags=re.M)[1:]
                self.assertEqual(len(chunks), 20)
                # Prevent rote test-taking based on A/B/C/D cycling in groups of four.
                answer_letters = []
                for q_number, chunk in enumerate(chunks, 1):
                    choices = re.findall(r"^([ABCD])\. (.+)$", chunk, flags=re.M)
                    answer = re.findall(r"^\*\*Đáp án: ([ABCD])\*\*$", chunk, flags=re.M)
                    explanations = re.findall(r"^\*\*Giải thích:\*\* (.+)$", chunk, flags=re.M)
                    self.assertEqual([c[0] for c in choices], list("ABCD"))
                    self.assertEqual(len(answer), 1)
                    self.assertEqual(len(explanations), 1)
                    self.assertGreater(len(explanations[0]), 12)
                    self.assertEqual(len(set(text for _, text in choices)), 4)
                    answer_letters.append(answer[0])
                    if 5 <= q_number <= 8:
                        expected = answers[q_number - 5]
                        actual = dict(choices)[answer[0]]
                        self.assertEqual(actual, expected, f"{lesson_id}, Q{q_number}: wrong keyed choice")
                        self.assertGreaterEqual(len(explanations[0]), 45)
                        self.assertNotIn("Which function ", chunk.splitlines()[0])
                        reviewed += 1
                self.assertNotEqual("".join(answer_letters), "ABCD" * 5,
                                    f"{lesson_id}: answers are a predictable cycle")
        self.assertEqual(reviewed, 68)

if __name__ == "__main__":
    unittest.main()

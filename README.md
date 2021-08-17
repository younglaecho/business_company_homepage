# business page 수정사항



1. div 태그 background => image 태그로 바꾸기
   => 비율을 유지하면서 박스안에 딱맞게 들어오게만들기
   => div 안에 img 태그를 넣고, 이미지에서 길이가 긴쪽을 max로 설정한다. (각가의 div는 약간의 간격을 가짐.)
   => 이를 위해서는 원본 image의 높이와 너비를 구할 수 있어야 한다. => 이것을 위해 naturalWidth와 naturalHeight을 사용할 수 있다.


2.  lazy load 적용하기 
   => data-set에 고화질 이미지의 경로를 저장
   => src로 저화질 이미지를 먼저 띄움
   => 스크롤하여 현재이미지가 보이기 시작하면 src에 data-set의 경로를 입력하도록 함. 